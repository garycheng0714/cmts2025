🎯 CMTS 2025 是什麼？

它是加拿大的一個大型製造技術展覽，每兩年舉行一次。
世界博覽會下一屆在 2025 年 9 月 29 日到 10 月 2 日，地點在 多倫多會議中心（Toronto Congress Centre）。

它聚焦的是製造業裡的技術創新、機床工具、自動化、3D 列印、智慧製造等領域。
在展會中會有許多參展商（供應商、機械設備公司等）展示最新產品、技術演示、教育講座與論壇。


---------

從 CMTS 官網與公開資料，可以看到它所提供或能取得的主要內容包括：

| 類型                   | 說明／內容                                       | 用處                                  |
| -------------------- | ------------------------------------------- | ----------------------------------- |
| **參展商名錄 / 展商清單**     | 可查哪些公司將在展會中展出。             | 如果你是供應商、合作方，或要做資料擷取／分析，是很有用的目標清單    |
| **議程 / 教育講座 / 技術議題** | 有主題演講、論壇、技術專區（如智慧製造、增材製造）等。     | 如果你對技術趨勢、內容撰寫、報導或資料整合感興趣，可以從這些議程中取材 |
| **展會地圖 / 展場布局**      | 官網會有展場平面圖、展區分類等資訊。          | 對於參展或導航來說非常實用                       |
| **新產品發布 / 技術亮點**     | 展會會有「新產品發表」等專區或活動。             | 如果你負責技術、新品、趨勢報導，這是重點                |
| **新聞 / 媒體報導 /官方新聞稿** | 展會官方有新聞頁面來公布最新動向、亮點、統計數字等。    | 了解展會的主題變化、規模、參與者動態                  |
| **參觀者 / 來賓信息**       | 展會也介紹為什麼值得參加、參觀者能看見什麼、參觀者會有哪些收益。 | 若你是參與者或潛在客戶，就能判斷是否值得出席              |

--------

# What I Do

https://cmts2025.smallworldlabs.com/exhibitors

從 Excel 內拿取對應的展覽網址並爬取 360 個展覽資訊做資料清洗，並輸出為 json file

```
[
    {
        "Name": "3D Printing Canada",
        "What We Do": "At 3D Printing Canada, we specialize in industrial and commercial additive manufacturing solutions. As part of N3 Technologies Inc., we bring over 40 years of experience in advanced manufacturing, CNC machining, and industrial tooling to everything we do. Our mission is to help manufacturers, engineers, and product developers accelerate prototyping, improve part performance, and reduce production costs through cutting-edge 3D printing technologies. We supply a wide range of professional 3D printing systems, from desktop engineering workhorses to large-format industrial machines. Our lineup includes trusted brands like Bambu Lab, BigRep, Sinterit, Intamsys, Modix, Makerbot, Ultimaker, Vision Miner, and Caracol, covering FDM, resin, SLS, high-temp, and robotic extrusion technologies. Beyond printers, we offer one of Canada’s largest selections of industrial-grade filaments and resins. Our inventory includes high-performance materials such as carbon-fiber reinforced nylon, PEI/ULTEM, PEEK, ABS, ASA, PETG, and TPU, many compatible with multi-material systems and enclosed printers for demanding applications in aerospace, automotive, medical, and tooling environments. We also stock critical components, spare parts, nozzles, hotends, build platforms, and motion systems to support maintenance and performance upgrades. What sets us apart is our ability to support businesses beyond equipment sales: We offer custom print services for prototypes, short-run production, and functional end-use parts using high-performance materials and large-format systems. Our design team provides CAD modeling, consultation, print optimization, and engineering support for complex projects. We offer repair and maintenance services, technical onboarding, and in-depth training workshops to help your team adopt or scale additive manufacturing efficiently. We work closely with manufacturers, machine shops, engineers, research labs, educators, and startups across North America. Whether you're modernizing your prototyping workflow, improving supply chain flexibility, or building a digital inventory, we provide the technology, expertise, and service to make it happen. 3D Printing Canada isn’t just a reseller, we’re a strategic partner committed to advancing digital manufacturing for Canadian industry",
        "Founded": "2014",
        "Website": "https://3dprintingcanada.com",
        "Categories": "3D Printing / Additive Manufacturing",
        "Phone": "+1-905-963-9066",
        "Address": "36 Ditton Drive Unit 3 Hamilton, ON L8W 0A9 Canada",
        "Facebook": "https://www.facebook.com/3dprintingcanada",
        "Instagram": "https://www.instagram.com/3d.printing.canada/",
        "LinkedIn": "https://ca.linkedin.com/company/3d-printing-canada",
        "Twitter (X)": "https://twitter.com/3dprintingcan"
    },
    {
        "Name": "3Dconnexion & Optimum Arc",
        "What We Do": "3Dconnexion designs powerful, research-based ergonomic hardware and smart, easy-to-use software that combine seamlessly to make working in the world’s most popular CAD applications and 3D environments fast, comfortable and fun.",
        "Website": "https://3dconnexion.com/ca/",
        "Address": "Norwalk, CT 06854 United States",
        "Facebook": "https://www.facebook.com/3Dconnexion",
        "Instagram": "https://www.instagram.com/3dconnexion/",
        "LinkedIn": "https://www.linkedin.com/3Dconnexion",
        "Twitter (X)": "https://x.com/3Dconnexion/"
    },
    {
        "Name": "5MM Solution Inc",
        "What We Do": "custom machine and parts manufacturing ,metal and plastic parts ,gears and gear box ,welding 3D tables ,industry aluminium dissipator",
        "Website": "https://www.5m-ca.com",
        "Phone": "4375567918 whatsupp",
        "Address": "49 Chantilly Cres Richmond Hill, ON L4C 0K2 Canada"
    },
    {
        "Name": "7 Seas Sourcing LLC",
        "What We Do": "7 Seas Sourcing is a full-service, global sourcing provider that delivers quality, overseas manufacturing to our customers. Our experience and innovative vision can make any product a reality. We specialize in helping customers lower costs and improve quality by utilizing alternative manufacturing options.",
        "Website": "https://7seassourcing.com/",
        "Categories": "3D Printing / Additive Manufacturing, Automation – Fabrication, Bearings, Bolts, Bushings, Castings, Compressed Air Accessories & Components, Connectors, Contract Electronic Manufacturer, Control Wiring, Controllers & Regulators - Level, Pressure, Temperature, Couplings, Design and modeling of micro-systems, Dies, Electrical Control Products, Electronic Components, Enclosures, Extrusions, Fabrication Centres, Filters, Forgings, Industrial Contracting, Jigs & Fixtures, Laser Cutting Machines & Services, Metal Stamping, Prototyping, Pumps, Punches & Dies, Rapid Prototyping, Rollforming - Tooling, Machines, Screw Machine Products, Small Parts Machining, Steel - Tool & Die, Transmission / Driveline Components, Vacuums & Accessories, Valves, Wire & Cable, Wire Cutting, Product Design",
        "Phone": "734-357-8560",
        "Address": "43000 W 9 Mile Rd Ste 308 Novi, MI 48375-4129 United States"
    },
    ...
]
```
