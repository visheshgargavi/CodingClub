#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
region = field.getvalue('r')
sourceregion = field.getvalue('sr')
sourcesnapshot = field.getvalue('ss')

cmd = 'sudo /usr/local/bin/aws ec2 copy-snapshot --region {} --source-region {} --source-snapshot-id {} --description "My snapshot"'.format(region,sourceregion,sourcesnapshot)

output = sp.getoutput(cmd)
print(output)
