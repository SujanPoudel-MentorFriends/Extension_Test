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
        # print(data[4])
        return data[4]
    except:
        return []