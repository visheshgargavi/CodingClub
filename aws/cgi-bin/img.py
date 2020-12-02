#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()

cmd = "sudo docker images"
output = sp.getoutput(cmd)

print(output)
