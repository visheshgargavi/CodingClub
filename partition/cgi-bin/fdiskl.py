#!/usr/bin/python3
print("content-html: type/plain")
print()

import os
import subprocess as sp
import cgi

field = cgi.FieldStorage()

cmd = "sudo fdisk -l"
output = sp.getoutput(cmd)
print(output)
