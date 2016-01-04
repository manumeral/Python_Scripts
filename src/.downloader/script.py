import re
import urllib
url="http://www.pythonlearn.com/code/"
count = 0
page=urllib.urlopen(url);
for line in page:
	line=line.strip()
	found_src=re.findall('^<img .* <a href="(.*\.db?)"',line)
	found_name=re.findall('^<img .* <a href.*>(.*)<',line)
	if(len(found_src)>0):
		urllib.urlretrieve(url+found_src[0],found_name[0])
		print url+found_src[0]
		count+=1
print 'Nos. of files printed',count
