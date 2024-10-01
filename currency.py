import json
import requests


def get_currency_rate(currency_code: str):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    if response.status_code != 200:
        return False
    data_dict = response.json()
    x = data_dict.get('Valute').get(currency_code)


    json_data = json.dumps({"currency_code": x['CharCode'], "rate": x['Value']}, indent=4)
    return json_data

rate1 = get_currency_rate("USD")
print(rate1)
