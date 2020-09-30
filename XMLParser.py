#XML Parser
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_707172.xml'
parms = dict()
parms['address'] = address

url = urllib.parse.urlencode(parms)
print('Retrieving ', url)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
# Above this line functional and reading. 
sum = 0
for remark in tree.findall('.//count'):
	add = remark.text
	print(add)
	sum = int(add) + int(sum)
print(sum)

