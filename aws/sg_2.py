#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
securitygroupid = field.getvalue('sg')

cmd = 'sudo /usr/local/bin/aws ec2 describe-security-groups --group-ids {}'.format(securitygroupid)
output = sp.getoutput(cmd)
print(output)
