#!/usr/bin/env python3
from subprocess import check_output


saida = check_output(['ifconfig', 'enp2s0']).decode('utf-8')

if saida[32:39] == 'RUNNING':
    print('📶 ')

else:
    print('🚫 ')