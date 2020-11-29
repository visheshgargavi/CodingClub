#!/usr/bin/python3
print("content-type: type/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
disk = field.getvalue("d")
dest = field.getvalue("dir")

cmd = "sudo mount {} {}".format(disk,dest)
output = sp.getoutput(cmd)
print(output)
