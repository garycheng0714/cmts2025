from curl_cffi.requests.exceptions import RequestException
from tenacity import retry, stop_after_attempt, retry_if_exception_type, wait_exponential
from curl_cffi import AsyncSession
from bs4 import BeautifulSoup
from limiter import Limiter
import openpyxl, asyncio, json, re


limiter = Limiter(rate=1, capacity=5, consume=3)

async def get_exhibitor_info(url_list: list) -> list:
    result = []

    async with AsyncSession() as session:
        tasks = [fetch(session, url) for url in url_list]
        results = await asyncio.gather(*tasks)
        if results:
            result = results

    return result

@limiter
@retry(
    retry=retry_if_exception_type(RequestException),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    stop=stop_after_attempt(3),
)
async def fetch(session: AsyncSession, url: str) -> dict[str, str]:
    print(f"Fetching {url}")
    response = await session.get(url, impersonate="chrome")
    if response.status_code in [429, 500]:
        raise RequestException(status=response.status, message="Retry")

    return extract_data(response.text)

def extract_data(html: str) -> dict[str, str]:
    data = {}
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select("div[class='row small no-gutters mb-3']")

    for tag in tags:
        content = tag.select_one(".profileResponse").get_text(separator=" ", strip=True)
        clean_content = re.sub(r"\s+", " ", content).strip()
        data[tag.select_one(".text-secondary").text.strip()] = clean_content

    return data

def is_link(string: str) -> bool:
    return string.startswith("http")


if __name__ == '__main__':
    wb = openpyxl.load_workbook('scraping.xlsx')
    ws = wb.active

    column_b_cells = ws['B']

    url = [column_b_cells[i].value for i in range(len(column_b_cells))]

    exhibitor_info = asyncio.run(get_exhibitor_info(url))

    with open("exhibitors.json", "w", encoding="utf-8") as f:
        json.dump(exhibitor_info, f, ensure_ascii=False, indent=4)