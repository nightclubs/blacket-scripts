import requests
import time
import json

f = open("config.json")

config = json.load(f)
legacy_url = 'https://blacket.org/'

def add_tokens():
    with requests.Session() as session:
        token_res = session.post(
            legacy_url + 'worker/box/openbox.php',
            cookies = {
                'PHPSESSID': config['sessid'] # your sess id.
            },
            headers = {
                'authority': 'blacket.org',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://blacket.org',
                'pragma': 'no-cache',
                'referer': 'https://blacket.org/market/',
                'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
                'x-requested-with': 'XMLHttpRequest',
            },
            data = 'box=Add Tokens'
        )
        if "You're" in token_res.text:
           return 'Rate Limited..'
        else:
            return 'added 25k tokens!'

while True:
 time.sleep(config['time'])
 print(add_tokens())