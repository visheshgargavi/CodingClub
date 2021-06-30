#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
securitygroupid = field.getvalue('sg')
securitygroupname = field.getvalue('nsg')
protocol = field.getvalue('pro')
port = field.getvalue('port')
cidr = field.getvalue('cidr')

cmd = 'sudo /usr/local/bin/aws ec2 authorize-security-group-ingress --group-id {} --group-name {} --protocol {} --port {} --cidr {}'.format(securitygroupid,securitygroupname,protocol,port,cidr)

output = sp.getoutput(cmd)
print(output)
