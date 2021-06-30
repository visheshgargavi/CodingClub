#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
securitygroupname = field.getvalue('nsg')
desc =  field.getvalue('dsc')
vpcid = field.getvalue('vp')

cmd = 'sudo /usr/local/bin/aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(securitygroupname,desc,vpcid)
output = sp.getoutput(cmd)
print(output)
