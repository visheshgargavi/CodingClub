#!/usr/bin/python3
print("content-text: text/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
lname = field.getvalue("l")
osname = field.getvalue("osn")
i_name = field.getvalue("i")
version = field.getvalue("v")

cmd = "sudo docker run -dit --link {} --name {} {}:{}".format(lname,osname,i_name,version)
output = sp.getoutput(cmd)

print(output)
