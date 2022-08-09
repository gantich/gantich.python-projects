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
	username = dni # + letra
	passwordLength = random.randint(6, 10)
	password = ''.join(random.choice(chars) for i in range(passwordLength))
	r = requests.post(url, allow_redirects=False, data={
        'captcha': '',
        'step': 'login',
		'username': username,
		'password': password
	})
	
	print(r.status_code,': Enviando DNI',username,"y contraseña", password)