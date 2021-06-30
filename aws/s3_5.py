#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()

bucketname = field.getvalue('bn')
pic = sp.getvalue('p')

cmd = 'sudo /usr/local/bin/aws s3api delete-object --bucket {} --key {}'.format(bucketname,pic)
output = sp.getoutput(cmd)
print(cmd)
