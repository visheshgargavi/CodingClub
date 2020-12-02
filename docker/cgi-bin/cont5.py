#!/usr/bin/python3
print("content-text: text/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
network = cgi.FieldStorage("n")
osname = field.getvalue("osn")
i_name = field.getvalue("i")
version = field.getvalue("v")

cmd = "sudo docker run -dit --name {} --network {} {}:{}".format(osname,network,i_name,version)
output = sp.getoutput(cmd)

print(output)
