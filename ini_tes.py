import requests

proxy = {
    "http": 'http://185.61.152.137:8080',
}
url = "https://httpbin.org/ip"
#url_data = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=10"
#scraper = cloudscraper.create_scraper()
response = requests.get(url, proxies=proxy)
print(response.json())
