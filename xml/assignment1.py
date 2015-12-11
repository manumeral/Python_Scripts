import urllib
import xml.etree.ElementTree as ET

service_url='http://maps.googleapis.com/maps/api/geocode/xml?'

while(True):
	address=raw_input('Enter Location: ')
	if(len(address)<1):
		break

	url=service_url+urllib.urlencode({'sensor':'false','address':address})
	print 'Retrieving',url
	uh=urllib.urlopen(url)
	data=uh.read()
	print 'Retrieved',len(data),'characters'
	print data
	tree=ET.fromstring(data)

	results=tree.findall('results')
	lat=results[0].find('geometry').find('location').find('lat').text
	lang=results[0].find('geometry').find('location').find('lng').text
	location=results[0].find('formatted_address').txt
	
	print 'lat',lat,'lng',lang
	print location

