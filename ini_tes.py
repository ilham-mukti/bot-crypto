import requests

proxy = {
    "http": 'http://8.219.97.248:80',
    "https": 'https://8.219.97.248:80'
}
url = "https://httpbin.org/ip"
url_data = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=10"
#scraper = cloudscraper.create_scraper()
response = requests.get(url_data, proxies=proxy)
print(response.json())
