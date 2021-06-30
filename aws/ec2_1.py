#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()

cmd = 'sudo /usr/local/bin/aws ec2 describe-instances'
output = sp.getoutput(cmd)
print(output)
