#!/usr/bin/env python3
from httpx import get

url = get('https://api.hgbrasil.com/finance')
btc_icon = '₿'

if url.status_code == 200:
    dados = url.json()
    btc = dados.get('results').get('currencies').get('BTC').get('buy')
    print(f'{btc_icon} {btc} BRL')