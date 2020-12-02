#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
v_name = field.getvalue("vn")

cmd = "sudo docker volume create {}".format(v_name)
output = sp.getoutput(cmd)

print(output)
