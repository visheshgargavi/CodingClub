#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
instanceid = field.getvalue("it")
aminame = field.getvalue("an")
desc = field.getvalue("dsc")

cmd =  'sudo /usr/local/bin/aws ec2 create-image --instance-id {} --name "{}" --description "{}"'.format(instanceid,aminame,desc)

output = sp.getoutput(cmd)
print(output)
