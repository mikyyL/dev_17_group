import requests

# headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
# }
# url = 'https://httpbin.org/headers'
# response = requests.get(url, headers=headers)
# print(response.text)


data = {
        'custname': 'artem',
        'custtel': '123131321',
        'custemail': 'root@gmail.com',
        'size': 'small',
        'topping': 'bacon',
        'delivery': '20:45',
        'comments': 'faster'
}
url = 'https://httpbin.org/post'
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())


