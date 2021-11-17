import requests
import os
import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))


url = 'https://lightweightsolutions.co/wp-admin/js/widgets/sp/index.php'
i = 0
while i < 1:
	dni = ''.join(random.choice(string.digits) for i in range(8))
	letra = ''.join(random.choice(string.ascii_letters))
	username = dni + letra
	password = ''.join(random.choice(chars) for i in range(8))


	four = ''.join(random.choice(string.digits) for i in range(4))
	mm = str(random.randint(1, 12))
	yy = str(random.randint(21, 28))
	cv = ''.join(random.choice(string.digits) for i in range(3))
	requests.post(url, allow_redirects=False, data={
        'captcha': '',
        'step': 'cc',
		'four': four,
		'mm': mm,
		'yy': yy,
		'cv': cv,
	})
	
	print('Enviando 4 dígitos ',four,' con fecha ', mm ,'/', yy ,' y CV ',cv)

