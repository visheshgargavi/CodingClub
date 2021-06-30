#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
volumeid = field.getvalue('vid')
desc = field.getvalue("dsc")

cmd = 'sudo /usr/local/bin/aws ec2 create-snapshot --volume-id {} --description "{}"'.format(volumeid,desc)
output = sp.getoutput(cmd)
print(output)
