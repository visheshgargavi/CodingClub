#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
volumeid = field.getvalue('vid')

cmd = 'sudo /usr/local/bin/aws ec2 detach-volume --volume-id {}'.format(volumeid)
output = sp.getoutput(cmd)
print(output)
