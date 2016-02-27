#Temp

#Send information to laptop
import urllib
import urllib2
import json

my_mac = '192.168.1.105:8889'

url = 'http://' + my_mac + '/'



url = url + '?greeting={"23":23}'

req = urllib2.Request(url)
f = urllib2.urlopen(req)
response = f.read()
print(response)
f.close()

howdy = "123456789,"
trim_a = len(howdy)-1
howdy = howdy[:trim_a]
print(howdy)