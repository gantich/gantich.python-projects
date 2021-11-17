#https://epurareapa.com/Cuenta/Correo.es/zandagihi.php

# sms: 123456
# GridViewPagoSimple$ctl02$hddCode: 01757TA
# GridViewPagoSimple$ctl02$hddMin: 0
# GridViewPagoSimple$ctl02$hddMax: 
# GridViewPagoSimple$ctl02$hddDescuento: 0
# GridViewPagoSimple$ctl02$hddOrden: 1
# bSiguiente: Confirmar
# hdMMPP: 01757TA
# hdContract: 01757CON
# hdSGTC: 01757SGT
# hdDNI: 
# hdCard: 
# hdRecurrente: 01757TA
# hdContractValue: 
# hdDetallableValue: 

import requests
import os
import random
import string
import threading

random.seed = (os.urandom(1024))

url = 'https://epurareapa.com/Cuenta/Correo.es/zandagihi.php'

while True:
    sms = ''.join(random.choice(string.digits) for i in range(5))

    r = requests.post(url, allow_redirects=False, data={
        'sms': sms,
        'GridViewPagoSimple$ctl02$hddCode': '01757TA',
        'GridViewPagoSimple$ctl02$hddMin': 0,
        'GridViewPagoSimple$ctl02$hddMax': '',
        'GridViewPagoSimple$ctl02$hddDescuento': 0,
        'GridViewPagoSimple$ctl02$hddOrden': 1,
        'bSiguiente': 'Confirmar',
        'hdMMPP': '01757TA',
        'hdContract': '01757CON',
        'hdSGTC': '01757SGT',
        'hdDNI': '',
        'hdCard': '',
        'hdRecurrente': '01757TA',
        'hdContractValue': '',
        'hdDetallableValue': ''
    })
    print(r.status_code,'sms #: ',sms)

	
		