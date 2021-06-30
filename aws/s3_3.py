#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
bucketname = field.getvalue('bn')
pic = field.getvalue('p')

cmd = 'sudo /usr/local/bin/aws s3api put-object-acl --bucket {} --key {} --acl public-read'.format(bucketname,pic)
output = sp.getoutput(cmd)
print(cmd)
