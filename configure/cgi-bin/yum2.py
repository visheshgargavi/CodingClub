#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess

form=cgi.FieldStorage()
pss=form.getvalue("p")
ip=form.getvalue("i")
cmd = "sudo echo {} | sudo /usr/local/bin/ansible-playbook /var/www/cgi-bin/yum.yml --extra-vars 'Host={}'".format(pss,ip)
output=subprocess.getoutput(cmd)
print(output, end='')
status=output[0]
out=output[1]

if status==0:
  print("YUM CONFIGURED SUCCESSFULLY")
else:
  print("SORRRY!!")
