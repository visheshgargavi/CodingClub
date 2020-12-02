#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
n_name = field.getvalue("nnn")

cmd = "sudo docker network create {}".format(n_name)
output = sp.getoutput(cmd)

print(output)
