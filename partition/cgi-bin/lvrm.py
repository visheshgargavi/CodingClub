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
lv = field.getvalue("lv")
disk = field.getvalue("d")
size = field.getvalue("s")

cmd = "echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi=bin/lvremove.yml --extra-var 'Host={} Vgname={} Lvname={} Disk={} Size={}'".format(pss,ip,vg,lv,disk,size)

output = sp.getoutput(cmd)
print(output)
