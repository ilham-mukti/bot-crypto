import requests

url_data = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=10"
response = requests.get(url_data).json()
print(response)
