#!/usr/bin/env python3
from subprocess import check_output


saida = check_output(['ip','link', 'show', 'enp2s0']).decode('utf-8')

if 'state UP' in saida:
    print('📶 ')
    
else:
    print('🚫 ')
