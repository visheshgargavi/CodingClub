#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
bucketname = field.getvalue('bn')
region = field.getvalue('r')

cmd = 'sudo /usr/local/bin/aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(bucketname,region,region)
output = sp.getoutput(cmd)
print(cmd)
