import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
headers = {'user-agent': user}
url = 'https://browser-info.ru/'
response = requests.get(url, headers=headers)
page_html = response.text
# print(page_html)
# with open('info_browser.html', 'w') as file:
#     file.write(page_html)

soup = BeautifulSoup(page_html, 'lxml')
main_block = soup.find('div', id='tool_padding')
title = soup.title
print(title.text)
# print(main_block)
# js_block = main_block.find('div', id='javascript_check')
# print(js_block)
# list_js_result = js_block.find_all('span')
# print(list_js_result)
# js_text = list_js_result[0].text
# status_js_text = list_js_result[1].text
# print(f'{js_text} - {status_js_text}')

# Flash, User-agent
flash_block = main_block.find('div', id='flash_version')
print(flash_block)
list_flash_result = flash_block.find_all('span')
print(list_flash_result)
flash_text = list_flash_result[0].text
status_flash_text = list_flash_result[1].text
print(f'{flash_text} - {status_flash_text}')

user_agent_block = main_block.find('div', id='user_agent')
print(user_agent_block)
text_user_agent = user_agent_block.find('span', {'class': 'option_title'}).text
print(f'{user_agent_block.text}')
