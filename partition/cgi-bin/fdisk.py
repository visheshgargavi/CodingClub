#!/usr/bin/python3
print("content-html: type/plain")
print()

import os
import subprocess as sp
import cgi

field = cgi.FieldStorage()
disk = field.getvalue("d")

cmd = "sudo fdisk {}".format(disk)
output = sp.getoutput(cmd)
print(output)
