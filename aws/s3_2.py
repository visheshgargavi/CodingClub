#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
loc = field.getvalue('l')
bucketname = field.getvalue('bn')

cmd = 'sudo /usr/local/bin/aws s3 sync "{}" s3://{}'.format(loc,bucketname)
output = sp.getoutput(cmd)
print(cmd)
