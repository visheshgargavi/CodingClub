#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
osname = field.getvalue("osn")
cmd = field.getvalue("c")
name = field.getvalue("nn")

cmd = "sudo docker exec -i {} {} {}".format(osname,cmd,name)
output = sp.getoutput(cmd)

print(output)
