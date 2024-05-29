#!/usr/bin/env python3
from httpx import get

url = get('https://api.hgbrasil.com/finance')
dolar_icon ='💲'

if url.status_code == 200:
    dados = url.json()
    dolar_brl = dados.get('results').get('currencies').get('USD').get('buy')
    print(f'{dolar_icon} {round(dolar_brl,2)} BRL')