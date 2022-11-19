import requests
import random
import json
import time

f = open("config.json")

config = json.load(f)
legacy_url = 'https://blacket.org/'
box_types = ['Aquatic', 'Blizzard', 'Color', 'Dino', 'Ice Monster', 'Medieval', 'Safari', 'Space', 'Spooky', 'Wonderland']

def buy_boxes():
    with requests.Session() as session:
        box = random.choice(box_types)
        box_res = session.post(
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
            data = {
                'box': box
            }
        )
        if box in box_res.text:
            box_type = box_res.text.split('|')[0]; box_rarity = box_res.text.split('|')[1]
            open('./boxes/bought.txt', 'a').write('%s:%s\n' % (box_type, box_rarity)); return 'Successfully bought %s box and received %s (%s)!' % (box, box_type, box_rarity)

        elif "You're being rate limited.":
            return 'Rate Limited..'

        

while True:
 time.sleep(config['time'])
 print(buy_boxes())