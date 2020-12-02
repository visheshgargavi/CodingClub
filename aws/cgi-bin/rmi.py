#!/usr/bin/python3
print("content-text: text/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
i_name = field.getvalue("i")

cmd = "sudo docker rmi {}".format(i_name)
output = sp.getoutput(cmd)

print(output)
