#!/usr/bin/python3
print("content-type: type/plain")
print()

import os
import cgi
import subprocess as sp

field = cgi.FieldStorage()
pss = field.getvalue("p")
user =field.getvalue("h")
x = field.getvalue("c")

cmd = 'echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/hadoop-basic.yml --extra-vars "Host={} cmd={}"'.format(pss,user,x)
output = sp.getoutput(cmd)
print(output)
