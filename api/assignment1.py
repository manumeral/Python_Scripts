import json
import urllib
import json

service_url = raw_input('Enter a url:')
handle=urllib.urlopen(service_url).read()

info = json.loads(handle)
#print json.dumps(info,indent=4)

print sum(int(item['count']) for item in info['comments'])
