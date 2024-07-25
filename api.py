import requests
from time import sleep
import os

# base_url = os.environ.get('BASE_URL')
base_url = "https://theta.boomconcole.com/api/v1"
print(f"BASE_URL: {base_url}")

url = base_url + "/extension-dom"

def fetch_api():
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        data = response.json()

        dom = {
            "chatgpt" : data[0],
            "poe_chat" : data[1],
            "you_chat" : data[2],
            "bard" : data[3],
            "linkedin" : data[4],
            "indeed" : data[5],
            "maps" : data[6]
        }
        # print(data[4])
        return dom
    except:
        return []