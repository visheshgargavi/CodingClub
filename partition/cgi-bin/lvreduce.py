#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
pss = field.getvalue("p")
ip = field.getvalue("i")
vg = field.getvalue("vg")
lv = field.getvalue("lv")
size = field.getvalue("s")

cmd = "echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/lvreduce.yml --extra-var 'Host={} Vgname={} Lvname={} Size={}'".format(pss,ip,vg,lv,size)

output = sp.getoutput(cmd)
print(output)
