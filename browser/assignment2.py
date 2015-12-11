import urllib2
from BeautifulSoup import *
import ssl
import re

page="https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Nicholas.html"
gcontext=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
for x in range(7):
	html=urllib2.urlopen(page,context=gcontext).read()
	soup=BeautifulSoup(html)
	tags=soup('a')
	page=(re.findall('href="(.*)"',str(tags[17])))[0]
	print re.findall('^<a .*>(.*)<',str(tags[17]))[0]
