
#!/usr/bin/python

import sys
import requests, json
import subprocess


url = 'http://10.75.50.23:8080/job/petclinic/lastBuild/api/json'
r = requests.get(url)


out_str = r.text
data = json.loads(out_str)
status = data['result']

if status != 'SUCCESS' :
	print "FAILED=================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	print "FAILED=================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	print "FAILED=================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	process = subprocess.Popen(['python', '/root/pravash/createincident.py'])
else :
	print "SUCCESS"


