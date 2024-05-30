#!/usr/bin/env python3
from httpx import get

url = get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
btc_icon = '₿'

if url.status_code == 200:
    dados = url.json()
    btc_brl = dados['BTCBRL']['bid']
    print(f'{btc_icon} {btc_brl} BRL')
