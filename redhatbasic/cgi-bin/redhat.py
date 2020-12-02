#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
myx = field.getvalue("x")


x = sp.getstatusoutput("sudo " + myx)
status = x[0]
output = x[1]
if status == 0:
  print(output)
else:
  print("command not found")
