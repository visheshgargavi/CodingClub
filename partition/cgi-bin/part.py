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
start = field.getvalue("s")
end = field.getvalue("e")

cmd = "sudo echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/static.yml --extra-vars 'Host={} Device={} Number={} start={} end={}'".format(pss,host,disk,num,start,end)
output = sp.getoutput(cmd)
print(output)
