import requests
import cloudscraper

proxy = {
    "http": 'http://103.214.54.254:8080',
}
url_data = "https://www.tokocrypto.com/v1/market/trading-pairs?quoteAsset=USDT&offset=0&limit=10"
scraper = cloudscraper.create_scraper()
response = scraper.get(url_data)
print(response.json())
