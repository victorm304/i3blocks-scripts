#!/usr/bin/env python3
from httpx import get

url = get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
dolar_icon ='💲'

if url.status_code == 200:
    dados = url.json()
    dolar_brl = dados['USDBRL']['bid']
    print(f'{dolar_icon} {dolar_brl[0:4]} BRL')
