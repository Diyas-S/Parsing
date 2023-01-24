import json
import requests
from headers import headers
from bs4 import BeautifulSoup

smartphone = []

for i in range(14):
    url = "https://shop.kz/smartfony/filter/astana-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1="+str(i+1)
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html5lib')

    all_block = soup.find_all('div', {"class": "bx_catalog_item_container gtm-impression-product"})
    for block in all_block:
        name = block.find('h4', {"class": 'bx_catalog_item_title_text'}).text
        article = block.find('div', {"class": 'bx_catalog_item_XML_articul'}).text.strip()[9:]
        memory = name[name.find(",") + 2: name.rfind(",")]
        try:
            price = block.find('span', {"class": 'bx-more-price-text'}).text.replace(" ", "")[:-1]
        except:
            price = "Нет в наличии"

        smartphone.append({
            'name': name,
            'article': article,
            'price': price,
            'memory-size': memory
        })
    print(i)
with open("smartphones_json", 'w') as file:
    json.dump(smartphone, file, indent=2)
