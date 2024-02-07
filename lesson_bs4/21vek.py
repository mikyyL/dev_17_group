import requests
from bs4 import BeautifulSoup
import fake_useragent

url = 'https://www.21vek.by/mobile/iphone_15/'
user = fake_useragent.UserAgent().random
headers = {'user-agent': user}
response = requests.get(url, headers=headers)
page_html = response.text

soup = BeautifulSoup(page_html, 'lxml')
# first_tel_block = soup.find('div', {'data-id': 'product-8623106'})
# print(first_tel_block)
# block_p = first_tel_block.find_all('p')
# print(block_p)
# price_text = block_p[0].text
# name_tel = block_p[1].find('a').text
# print(f'Цена телефона {name_tel} составляет {price_text}')
category_block = soup.find('div', {'class': 'styles_items__cGwBZ'})
print(category_block)
tags_categories_list = category_block.find_all('a')
print(tags_categories_list)
categories_list = []
for i in tags_categories_list:
    categories_list.append(i.text)

print(categories_list)


