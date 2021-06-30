#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
volumesize = field.getvalue('vs')
volumeid = field.getvalue('vid')

cmd = 'sudo /usr/local/bin/aws ec2 modify-volume --size {} --volume-id {}'.format(volumesize,volumeid)
output = sp.getoutput(cmd)
print(output)
