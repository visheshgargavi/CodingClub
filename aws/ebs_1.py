#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
volumetype = field.getvalue('vt')
volumesize = field.getvalue('vs')
avazone = field.getvalue('az')

cmd = 'sudo /usr/local/bin/aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(volumetype,volumesize,avazone)
output = sp.getoutput(cmd)
print(output)
