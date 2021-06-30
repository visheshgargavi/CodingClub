#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
key = field.getvalue('k')

cmd = 'sudo /usr/local/bin/aws ec2 create-key-pair --key-name {}'.format(k)
output = sp.getoutput(cmd)
print(cmd)
