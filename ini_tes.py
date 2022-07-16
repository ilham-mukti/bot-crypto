import requests

proxy = {
    "http": 'http://103.214.54.254:8080',
}
s = requests.Session()
url_data = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=10"
response= s.get(url_data, proxies=proxy).json()
print(response)
