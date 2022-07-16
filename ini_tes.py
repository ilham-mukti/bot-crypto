import requests

url_data = "https://www.binance.info/bapi/composite/v1/public/marketing/symbol/list"
response = requests.get(url_data).json()
print(response)
