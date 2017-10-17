#import urllib2
 
#request = urllib2.Request("http://v.mifile.cn/")
#try:
#	response = urllib2.urlopen(request)
#except urllib2.HTTPError,e:
	 
#	 print e.code
#	 print e.reason
#else:
#	print response.read()
	
import urllib2
req = urllib2.Request("http://v.mifile.cn/")
try:
	urllib2.urlopen(req)
except urllib2.HTTPError,e:
	print e.code
except urllib2.URLError,e:
	print e.reason
else:
	print "OK"

