#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
lvname = field.getvalue("lv")
vgname = field.getvalue("vg")
size = field.getvalue("s")

cmd = "sudo lvcreate --size {} --name {} {}".format(size,lvname,vgname)
output = sp.getoutput(cmd)
print(output)
