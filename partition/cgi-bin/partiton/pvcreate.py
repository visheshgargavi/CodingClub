#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
disk = field.getvalue("d")

cmd = "sudo pvcreate {}".format(disk)
output = sp.getoutput(cmd)
print(output)
