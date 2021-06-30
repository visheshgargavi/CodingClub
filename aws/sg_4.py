#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
securitygroupid = field.getvalue('sg')
protocol = field.getvalue('pro')
port = field.getvalue('port')
cidrblock = field.getvalue('cidr')

cmd = 'sudo /usr/local/bin/aws ec2 authorize-security-group-egress --group-id {}  --protocol {} --port {} --cidr {}'.format(securitygroupid,protocol,port,cidrblock)
output = sp.getoutput(cmd)
print(output)
