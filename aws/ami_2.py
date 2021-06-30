#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
amiid = field.getvalue("ai")

cmd = 'sudo /usr/local/bin/aws ec2 deregister-image --image-id {}'.format(amiid)

output = sp.getoutput(cmd)
print(output)
