import json
import requests

api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

r = requests.get(api_url)
info = r.json()
print('REALTIME BTC PRICES')
print('--------------------------')
time = "Time: " + info['time']['updated']
print(time)
usd = info['bpi']['USD']['rate']
print('1 BTC = ' + 'USD ' + usd)
gbp = info['bpi']['GBP']['rate']
print('1 BTC = ' + 'GBP ' + gbp)
eur = info['bpi']['EUR']['rate']
print('1 BTC = ' + 'EUR ' + eur)
