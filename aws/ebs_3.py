#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
instanceid = field.getvalue('id')
volumeid = field.getvalue('vid')
devicename = field.getvalue('dvn')

cmd = 'sudo /usr/local/bin/aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(instanceid,volumeid,devicename)
output = sp.getoutput(cmd)
print(output)
