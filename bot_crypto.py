import requests
import os 
import json
import ast
import datetime

class BotCrypto:
    def __init__(self):
        self.output_file = "harga_lama.json"
        self.params = {
            'quoteAsset': 'USDT',
            'offset': '0',
            'limit': '1000',
        }

        self.headers = {
            'authority': 'www.tokocrypto.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'device': '4',
            'deviceno': 'b33ad919cf38f746bea88654d039769a',
            'language': 'id',
            'referer': 'https://www.tokocrypto.com/markets',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-trace-id': 'a917dd74-d1b0-4104-9848-69193501c1b0',
        }

    def request_data(self):
        s = requests.Session()
        url_data = "https://www.tokocrypto.com/v1/market/trading-pairs"
        response = s.get(url_data, params=self.params, headers=self.headers)
        response = response.json()
        results = response['data']['list']

        my_dict = {}
        for data in results:
            name_pairs = data['symbol']
            price = float(data['price'])
            my_dict[name_pairs] = price
        return my_dict
            
    def create_file(self, data):
        f = open(self.output_file, 'w')
        f.write(str(data))
        f.close()
        print("selesai")

    def olah_data(self, harga_baru):
        is_new = not os.path.isfile(self.output_file)
        if is_new:
            self.create_file(harga_baru)
        else:
            print("file sudah ada")
            f = open(self.output_file, 'r')
            read_data = f.read()
            harga_lama = ast.literal_eval(read_data)
            diff = {key: round((harga_baru[key] - harga_lama.get(key, 0))/harga_lama.get(key, 0)*100, 2) for key in harga_baru.keys()}

            dict_coin_up = {}
            for key, value in diff.items():
                if value >= 0.2:
                    print(f"{key} -> {value} -> Buy")

                    dict_coin_up[key] = value
                    # Update Readme with the new data!

            f.close()
            self.create_file(harga_baru)
            self.update_readme(dict_coin_up)

    def update_readme(self, data):
        now = datetime.datetime.now()
        with open('readme.md', 'w') as f:
            f.write(f"# Data koin yang naik cepat {now}\n\n")

            for key, value in data.items():
                f.write(f'* {key} -> Meningkat {value}%\n')
            f.close()

bot = BotCrypto()
data_raw = bot.request_data()
result = bot.olah_data(data_raw)
