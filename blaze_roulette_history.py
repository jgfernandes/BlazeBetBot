import requests
import time
from random import choice

s = requests.Session()
s.trust_env = False
page_source2 = []

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
def random_headers():
    return {'User-Agent': choice(desktop_agents)}
ua = random_headers()

for a in range(99999999999999999999999999999):
    ua
    print(ua)
    for a in range(1):
        try:
            r = s.get("https://blaze.com/api/roulette_games/recent",headers=ua)
            page_source = r.content
        except:
            time.sleep(5)
            print("5")
            r = s.get("https://blaze.com/api/roulette_games/recent",headers=ua)
            page_source = r.content
        if page_source == page_source2:
            print("Same results, wait.")
            time.sleep(9)
            print("9")
        else:
            print("New Result!")
            print(r.status_code)
            try:
                j = r.json()[0]
            except:
                pass
            print(j)
            id = j["id"]
            created_at = j["created_at"]
            color = j["color"]
            roll = j["roll"]
            server_seed = j["server_seed"]
            dados = f"{id};{created_at};{color};{roll};{server_seed}\n"
            with open('blaze_history.txt', 'a') as f:
                f.write(dados)
                f.close
            print(dados)
            time.sleep(9)
            print("9!")
            page_source2 = r.content
       
