#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
securitygroupid = field.getvalue('sg')

cmd = 'sudo /usr/local/bin/aws ec2 delete-security-group --group-id {}'.format(securitygroupid)

output = sp.getoutput(cmd)
print(output)
