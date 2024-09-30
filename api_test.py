import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env-файла
load_dotenv()
# Получение значения переменной GITHUB_TOKEN из .env-файла
API_KEY = os.getenv('API_KEY')



from_ = 'USD'
to =  'RUB'
amount =  100

url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

payload = {}
headers= {
  "apikey": API_KEY
}

response = requests.request("GET", url, headers=headers, data = payload)
# response = requests.get(url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)
