import requests

# url = 'https://reqres.in/api/users/2'
# response = requests.get(url)
# print(response.status_code)
# print(response.json())

# data = {
#     "name": "morpheus",
#     "job": "leader"
# }
#
# url = 'https://reqres.in/api/users'
# response = requests.post(url, data=data)
# print(response.status_code)
# print(response.json())

# url = 'https://reqres.in/api/users/2'
# data = {
#     "name": "morph",
#     "job": "zion resident"
# }
#
# response = requests.patch(url, data=data)
# print(response.status_code)
# print(response.json())

# url = 'https://reqres.in/api/users/2'
# response = requests.delete(url)
# print(response.status_code)


url = 'https://reqres.in/api/register'
data = {
    "email": "eveeee.holt@reqres.in",
    "password": "pistolll"
}
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())
