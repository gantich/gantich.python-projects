import os
import threading

threadCount = 50

def do_request():
    while True:
        print('hello')

threads = []

for i in range (threadCount):
		t = threading.Thread(target=do_request)
		t.daemon = True
		threads.append(t)

for i in range(threadCount):
	threads[i].start()

for i in range(threadCount):
	threads[i].join()	