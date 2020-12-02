#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
pss = field.getvalue("p")
user = field.getvalue("h")
n_dir = field.getvalue("ndir")
n_ip = field.getvalue("nip")
port = field.getvalue("port")

cmd = "echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/namenode.yml --extra-vars 'Host={} n_dir={} n_ip={} hadoop_port={}'".format(pss,user,n_dir,n_ip,port)

output = sp.getoutput(cmd)
print(output)

