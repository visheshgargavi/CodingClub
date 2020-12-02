#!/usr/bin/python3
print("content-type: text/plain")
print()


import cgi
import subprocess as sp
import os


field = cgi.FieldStorage()
pss = field.getvalue("p")
ip = field.getvalue("i")
vg = field.getvalue("vg")
lv = field.getvalue("lv")
disk = field.getvalue("d")
size = field.getvalue("s")
fstype = field.getvalue("f")
src = field.getvalue("src")
dest = field.getvalue("dest")

cmd = "echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/lvm.yml --extra-vars 'Host={} Vgname={} Lvname={} Disk={} Size={} Fstype={} Src={} Dest={}'".format(pss,ip,vg,lv,disk,size,fstype,src,dest)

output = sp.getoutput(cmd)
print(output)
