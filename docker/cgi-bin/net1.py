#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
osname = field.getvalue("osn")
n_name = field.getvalue("nnn")

cmd = "sudo docker network connect {} {}".format(n_name,osname)
output = sp.getoutput(cmd)

print(output)
