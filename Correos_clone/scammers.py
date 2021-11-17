import requests
import os
import random
import string
import json
#import threading
import datetime


chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

saved_time = datetime.datetime.now()

url = 'https://epurareapa.com/Cuenta/Correo.es/pay.php'

credit_cards = json.loads(open('creditcards.json').read())

#def do_request():


while True:
	current_time = datetime.datetime.now()
	if (current_time - saved_time).seconds >= 10:
		saved_time = datetime.datetime.now()

		mm = str(random.randint(1, 12))
		yy = str(random.randint(21, 28))
		credit_card = ''.join(random.choice(credit_cards))
		cvv = ''.join(random.choice(string.digits) for i in range(3))
		
		password = ''.join(random.choice(chars) for i in range(8))

		r = requests.post(url, allow_redirects=False, data={
			'is_Numero_Tarjeta': credit_card,
			'Sis_Caducidad_Tarjeta_Mes': mm,
			'Sis_Caducidad_Tarjeta_Anno': yy,
			'Sis_Tarjeta_CVV2': cvv,
			'Sis_Divisa': '',
			'browserJavaEnabled': 'false',
			'browserLanguage': 'en-US',
			'browserColorDepth': 24,
			'browserScreenHeight': 680,
			'browserScreenWidth': 1365,
			'browserTZ': 0,
			'browserUserAgent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
			'threeDSCompInd': '',
			'bcancel': ''
		})
		print(r.status_code,'Card #: ',credit_card,' expires ',mm,'/',yy,' cvv ',cvv)

#threads = []

#for i in range (1):
#		t = threading.Thread(target=do_request)
#		t.daemon = True
#		threads.append(t)
#
#for i in range(1):
#	threads[i].start()
#
#for i in range(1):
#	threads[i].join()		