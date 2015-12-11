import urllib
import BeautifulSoup
import re

destination="http://python-data.dr-chuck.net/comments_210722.html"
html=(urllib.urlopen(destination))
total=0
lst=list()
#print html
for line in html:
	#print line
	line=line.strip()
	lst=lst+re.findall('<span .*>([0-9]+)',line)
print "Count",len(lst)
print "Sum",sum(int(x) for x in lst )
