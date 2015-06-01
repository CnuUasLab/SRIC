import urllib2
import os
import time

server = '192.168.1.1'
urllib2count = 0
pingcount = 0
tmp = 0
for x in range(0, 100):
	tmp = time.time()
	try:
	  connection = urllib2.urlopen('http://' + server, timeout = 1)       
	except urlib2.URLError as err:
	  pass
	urlib2count = time.time() - tmp

	tmp = time.time()
	result = os.system('ping -n 1 ' + server)
	pingcount = time.time() - tmp

print urlib2count / 100
print pingcount / 100
