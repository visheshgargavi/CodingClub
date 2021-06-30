#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
access = field.getvalue("a")
secret = field.getvalue("s")
region = field.getvalue("r")
frmat = field.getvalue("f")

cmd = 'sudo echo -ne "{}\n{}\n{}\n{}\n" | sudo /usr/local/bin/aws configure'.format(access,secret,region,frmat)
output = sp.getoutput(cmd)
print(output)
