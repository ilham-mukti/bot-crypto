import requests
import os 
import json
import ast
import datetime

class BotCrypto:
    def __init__(self):
        self.output_file = "harga_lama.json"
        self.cookies = {
            '__auc': '5403b3fa17e398e2cc193a7087e',
            'bnc-uuid': 'f6ce5435-9352-481e-b50c-d3a2d7db5403',
            '_ga': 'GA1.2.1257251472.1641643127',
            '__zlcmid': '17wkcChBqcNYPvg',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217e398e3275e88-08d0df2d6bd7fe-f791b31-1327104-17e398e3276fb6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217e398e3275e88-08d0df2d6bd7fe-f791b31-1327104-17e398e3276fb6%22%7D',
            '_tt_enable_cookie': '1',
            '_ttp': 'd2ebb47b-e49e-46ab-be5f-ec4063fa3f19',
            '_gcl_au': '1.1.867264609.1657271669',
            '_gid': 'GA1.2.1095833806.1657652758',
            'bc.trade.theme': 'dark',
            '__asc': '86c03c9818202f6c631859732ed',
            '_gat_gtag_UA_116825757_2': '1',
            'utag_main': "v_id:017f98f027d500223f9245452d0203072002b06a00978{_sn:170$_se:6$_ss:0$_st:1657909226572$dc_visit:30$ses_id:1657907103262%3Bexp-session$_pn:5%3Bexp-session$dc_event:6%3Bexp-session$dc_region:ap-east-1%3Bexp-session}",
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

        self.params = {
            'quoteAsset': 'USDT',
            'offset': '0',
            'limit': '1000',
        }

    def request_data(self):
        try:
            url_data = "https://www.tokocrypto.com/v1/market/trading-pairs"
            response = requests.get(url_data, params=self.params, cookies=self.cookies, headers=self.headers).json()
            results = response['data']['list']

            my_dict = {}
            for data in results:
                name_pairs = data['symbol']
                price = float(data['price'])
                my_dict[name_pairs] = price
            return my_dict
        except:
            print("tidak ada")
            
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
