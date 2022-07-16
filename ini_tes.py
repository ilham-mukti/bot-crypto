import requests

proxy = {
    "http": 'http://138.68.238.19/:31028',
    "http": 'http://170.39.194.16/:3128' 
}
s = requests.Session()
url_data = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=10"
response= s.get(url_data, proxies=proxy).json()
print(response)
