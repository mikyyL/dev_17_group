import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}
url_page = 'https://github.com/login'
url_auth = 'https://github.com/session'
data = {
    'login': 'mikyedit@gmail.com',
    'password': '',
    'authenticity_token': ''
}

with requests.Session() as session:
    response = session.get(url_page, headers=headers)
    login_page_html = response.text
    print(response)

    soup = BeautifulSoup(login_page_html, 'lxml')
    block_token = soup.find('input', {'name': 'authenticity_token'})
    token = block_token.get('value')
    print(token)
    data['authenticity_token'] = token
    response = session.post(url_auth, headers=headers, data=data)
    result = response.text
    # print(result)

with open('auth_page.html', 'w', encoding='utf-8') as file:
    file.write(result)