#!/usr/bin/env python3

from httpx import get

def kelvin_to_celsius(temp):
    return int(temp - 273.15)

# Icones
icone_sol = ""
icone_nuvem = ""
icone_chuva =""
icone_tempestade =""
icone_neve =""
icone_fog =""
simbolo_celsius = "°C" 


api_key = '032490db50ef4537bce870ec46b033ad'
city = 'Natal'
country = 'br'
lang = 'pt_br'
url = get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&lang={lang}&appid={api_key}')

if url.status_code == 200:
    dados = url.json()
    main = dados.get('weather')[0]['main']
    temp = kelvin_to_celsius(dados['main']['temp'])
    country = dados.get('sys').get('country')
    
    if main.startswith('Cloud'):
        print(f"{icone_nuvem}  {temp}{simbolo_celsius} - {city}/{country}")
    
    elif main.startswith('Rain'):
        print(f"{icone_chuva}  {temp}{simbolo_celsius} - {city}/{country}")
    
    elif main.startswith('Thunderstorm'):
        print(f"{icone_tempestade}  {temp}{simbolo_celsius} - {city}/{country}")
    
    elif main.startswith('Clear'):
        print(f"{icone_sol}  {temp}{simbolo_celsius} - {city}/{country}")
    
    elif main.startswith('Snow'):
        print(f"{icone_neve}  {temp}{simbolo_celsius} - {city}/{country}")
    
    elif main.startswith('Mist'):
        print(f"{icone_fog}  {temp}{simbolo_celsius} - {city}/{country}")
    
    elif main.startswith('Fog'):
        print(f"{icone_fog}  {temp}{simbolo_celsius} - {city}/{country}")
