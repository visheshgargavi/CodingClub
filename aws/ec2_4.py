#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
ami = field.getvalue('a')

cmd = 'sudo /usr/local/bin/aws ec2 terminate-instances --instance-ids {}'.format(ami)
output = sp.getoutput(cmd)
print(output)
