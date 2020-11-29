#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
disk = field.getvalue("d")
size = field.getvalue("s")

cmd = "sudo lvreduce --size {} {}".format(size,d)
output = sp.getoutput(cmd)
print(output)
