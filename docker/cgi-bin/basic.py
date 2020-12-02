#!/usr/bin/python3
print("content-text: text/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
basic = field.getvalue("b")

cmd = "sudo docker {}".format(basic)
output = sp.getoutput(cmd)

print(output)
