#!/usr/bin/python3
print("content-type: type/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
pss = field.getvalue("p")
ip = field.getvalue("i")
vg = field.getvalue("vg")

cmd = "echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi=bin/vgremove.yml --extra-var 'Host={} Vgname={}'".format(pss,ip,vg)

output = sp.getoutput(cmd)
print(output)
