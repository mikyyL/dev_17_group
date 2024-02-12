import requests
from bs4 import BeautifulSoup
data = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
response = requests.get('https://api.restful-api.dev/objects/ff8081818d8febd0018d9e4183080811')
print(response.json())
# response = requests.get('https://www.onliner.by/')
# html_onliner = response.text
#
# soup = BeautifulSoup(html_onliner, 'lxml')
# links = soup.find_all('a')
# # print(links)
# for link in links:
#     print(link.get('href'))
