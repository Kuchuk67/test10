import requests

from_ = 'USD'
to =  'RUB'
amount =  100

url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

payload = {}
headers= {
  "apikey": "AmjiF4XkH8CyU3qVWhLP2Gu3dSmVPNO1"
}

response = requests.request("GET", url, headers=headers, data = payload)
# response = requests.get(url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)
r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)
with open('comic.png', 'wb') as f:
    f.write(r.content)