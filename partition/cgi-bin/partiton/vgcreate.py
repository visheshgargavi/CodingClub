#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
name = field.getvalue("n")
disk = field.getvalue("d")

cmd = "sudo vgcreate {} {}".format(name,disk)
output = sp.getoutput(cmd)
print(output)
