#!/usr/bin/python3
print("content-text: text/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
osname = field.getvalue("osn")
vol1 = field.getvalue("v1")
vol2 = field.getvalue("v2")
i_name = field.getvalue("i")
version = field.getvalue("v")

cmd = "sudo docker run -dit --name {} -v {}:{} {}:{}".format(osname,vol1,vol2,i_name,version)
output = sp.getoutput(cmd)

print(output)
