#!/usr/bin/python3
print("content-type: type/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
ftype = field.getvalue("t")
disk = field.getvalue("d")

cmd = "sudo mkfs.{} {}".format(ftype,disk)
output = sp.getoutput(cmd)
print(output)
