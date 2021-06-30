#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
ami = field.getvalue('a')
instancetypes = field.getvalue('it')
count = field.getvalue('c')
subnet = field.getvalue('s')
securitygroupids = field.getvalue('sg')
key = field.getvalue('k')

cmd = 'sudo /usr/local/bin/aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(ami,instancetypes,count,subnet,securitygroupids,key)

output = sp.getoutput(cmd)
print(output)
