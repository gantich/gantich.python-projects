import requests
import os
import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
#https://lightweightsolutions.co/wp-admin/js/widgets/sp/index.php

url = 'https://lightweightsolutions.co/wp-admin/js/widgets/sp/index.php'
i = 0
while i < 1:
	sms = ''.join(random.choice(string.digits) for i in range(6))
	requests.post(url, allow_redirects=False, data={
        'captcha': '',
        'step': 'sms',
		'error': '',
		'sms_code': sms
	})

	print('Enviando sms', sms)