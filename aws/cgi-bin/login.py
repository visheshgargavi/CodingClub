#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
user = field.getvalue("usr")
passwd = field.getvalue("pss")

cmd = "sudo docker login --username {} --password {}".format(user,passwd)
output = sp.getoutput(cmd)

print(output)
