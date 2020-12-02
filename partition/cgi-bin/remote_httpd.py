#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
pss = field.getvalue("p")
host = field.getvalue("h")

cmd = "sudo echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/httpd.yml --extra-vars 'Host={}'".format(pss,host)
output = sp.getoutput(cmd)
print(output)
