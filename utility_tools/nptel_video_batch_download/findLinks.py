import re
import urllib
import subprocess
import sys
if(len(sys.argv)!=2):
	print "ERROR: python findLinks.py <url>\n expected exactly one argument"
	exit()
url=sys.argv[1]
#Test Link
#url='http://www.nptelvideos.in/2012/11/database-management-system.html'
lst=list()
count  = 0
page=urllib.urlopen(url)
for lines in page:
	line=lines.strip()
	found_src=re.findall("^<a href=\"javascript:loadvideo\(\'div[0-9]*\',\'frame[0-9]*\',\'(.*)\'\);",line)
	found_title=re.findall("^<a href=\"javascript:loadvideo.*>(.*)</a>",line)
	if(len(found_src) > 0):
		lst=lst+[(found_src[0],found_title[0],)]
		count += 1
fh=open("Lists_of_Lectures.txt","w")
url_base="https://www.youtube.com/watch?v="
for details in lst:
        url=url_base+details[0]
        name=details[1]
	#print url,name
	subprocess.call(["youtube-dl",url,"-o",name])
	fh.write(url+" "+name+"\n")
	
