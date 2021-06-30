#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
bucketname = field.getvalue('bn')

cmd = 'sudo /usr/local/bin/aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(bucketname)

output = sp.getoutput(cmd)
print(output)
