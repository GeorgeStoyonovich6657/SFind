#!/usr/bin/env python3

import requests
import sys
from concurrent.futures import ThreadPoolExecutor
import time

print(r"""


  /$$$$$$  /$$$$$$$$ /$$                 /$$
 /$$__  $$| $$_____/|__/                | $$
| $$  \__/| $$       /$$ /$$$$$$$   /$$$$$$$
|  $$$$$$ | $$$$$   | $$| $$__  $$ /$$__  $$
 \____  $$| $$__/   | $$| $$  \ $$| $$  | $$
 /$$  \ $$| $$      | $$| $$  | $$| $$  | $$
|  $$$$$$/| $$      | $$| $$  | $$|  $$$$$$$
 \______/ |__/      |__/|__/  |__/ \_______/
                                            

""")

print("[+] Welcome to SFind")

URL = sys.argv[1]
wordlist = sys.argv[2]

time.sleep(1)
print(f"[+] scanning {URL}")

def ping_site(URL):
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print(f"[+] {URL} is alive")
        else:
            print(f"[-] {URL} not found")
    except KeyboardInterrupt:
        sys.exit()
ping_site(URL)

with open(wordlist, "r") as f:
    words = [ word.strip() for word in f.readlines() ]

def scanning(URL):
    try:
        for word in words:
            response = requests.get(f"{URL}/{word}")
            if response.status_code == 200:
                print(f"[+] {word} found on server")
                if response.status_code != 200:
                    pass
    except requests.exceptions.ConnectionError:
        pass
    except KeyboardInterrupt:
        sys.exit()

with ThreadPoolExecutor(max_workers=100) as executor:
    scanning(URL)