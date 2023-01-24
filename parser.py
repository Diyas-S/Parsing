import json
import requests
from headers import headers
from bs4 import BeautifulSoup

smartphone = []

url = "https://shop.kz/smartfony/filter/astana-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1="
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'html5lib')


number_of_smartphones = int(soup.find("span", {"sort__count"}).text[:-8])
page_number = 1
while len(smartphone) != number_of_smartphones:
    url_smartphones = url + str(page_number)
    response = requests.get(url_smartphones, headers=headers).text
    soup = BeautifulSoup(response, 'html5lib')

    all_block = soup.find_all('div', {"class": "bx_catalog_item_container gtm-impression-product"})
    for block in all_block:
        name = block.find('h4', {"class": 'bx_catalog_item_title_text'}).text
        article = block.find('div', {"class": 'bx_catalog_item_XML_articul'}).text.strip()[9:]
        memory = name[name.find(",") + 2: name.rfind(",")]
        try:
            price_block = block.find("div", {"class": "bx-more-prices"}).text
            price_board = price_block.find("Цена в интернет-магазине")
            price = price_block[price_board + 24:price_board + 31].replace(" ", "")
            try:
                price = int(price)
            except ValueError:
                pass
        except Exception:
            price = "Нет в наличии"

        smartphone.append({
            'name': name,
            'articul': article,
            'price': price,
            'memory-size': memory
        })
    page_number += 1

with open("smartphones.json", 'w') as file:
    json.dump(smartphone, file, indent=2)
