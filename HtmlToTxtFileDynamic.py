import configparser
import requests
import time

config = configparser.ConfigParser()
config.read('Config.ini')
URL = config['Option']['url']
TIME = int(config['Option']['time'])
FILENAME = config['Option']['filename']

while True:
    text = requests.get(URL).text
    with open(FILENAME, "w", encoding='utf-8') as f:
        f.write(text)

    with open(FILENAME, "r", encoding='utf-8') as f:
        print(f.read())

    time.sleep(TIME)
