#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
pss = field.getvalue("p")
host = field.getvalue("h")
disk = field.getvalue("d")
num = field.getvalue("n")
src = field.getvalue("src")
end = field.getvalue("dest")

cmd = "sudo echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/rmstatic.yml --extra-vars 'Host={} Device={} Number={} src={} dest={}'".format(pss,host,disk,num,src,end)
output = sp.getoutput(cmd)
print(output)
