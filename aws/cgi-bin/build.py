#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
i_name = field.getvalue("i")
version = field.getvalue("v")
location = field.getvalue("loc")

cmd = "sudo docker build -t {}:{} {}".format(i_name,version,location)
output = sp.getoutput(cmd)

print(output)
