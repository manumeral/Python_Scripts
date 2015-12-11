import urllib
fhand=urllib.urlopen('https://www.messenger.com/t/binita.saha')

for lines in fhand:
	print line.strip()
