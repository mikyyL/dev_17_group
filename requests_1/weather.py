import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_token = 'de081f2ad84af3ccd0e1714937f56bad'
params = {'q': 'Minsk', 'appid': api_token}

response = requests.get(url, params=params)
print(response.status_code)
print(response.headers)
result_json = response.json()
a = 0
print(result_json)
print(result_json['name'])
print(result_json['sys']['country'])
print(result_json['main']['temp_min'])
print(result_json['main']['temp_max'])

# Получить значения ключей temp_min, temp_max, country, city
