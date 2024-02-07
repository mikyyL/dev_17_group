import requests

params = {'q': 'python'}
response = requests.get('https://www.google.com/search', params=params)
# print(response)
# статус код
# print(response.status_code)
# вывод заголовков
# print(response.headers)
# вывод содержимого нашего запроса
# print(response.text)
html_text = response.text
with open('html_google.html', 'w') as file:
    file.write(html_text)
