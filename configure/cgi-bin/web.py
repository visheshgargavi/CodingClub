#!/usr/bin/python3
print("content-type: text/html")
print()
import os
import subprocess
import cgi

y=cgi.FieldStorage()
o = y.getvalue("x")
print(o)
x=subprocess.getoutput("date")
print(x)
