import requests

# url = 'https://google-translate1.p.rapidapi.com/language/translate/v2/languages'
# headers = {
#     'Accept-Encoding': 'application/gzip',
#     'X-RapidAPI-Key': '46a60ddcfamsh735cfd849f48005p1f6015jsn9acf1c534c5d',
#     'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
# }
# params = {'target': 'ru', 'model': ''}
# response = requests.get(url, headers=headers, params=params)
# print(response.status_code)
# print(response.json())

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = {"q": "English is hard, but detectably so"}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "46a60ddcfamsh735cfd849f48005p1f6015jsn9acf1c534c5d",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
result = response.json()
language = result["data"]["detections"][0][0]['language']
print(f'{payload["q"]} - данная строка написана на {language} языке')
