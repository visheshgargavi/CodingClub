#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
volumetype = field.getvalue('vt')
snapshotid = field.getvalue('sid')
avazone = field.getvalue('az')

cmd = 'sudo /usr/local/bin/aws ec2 create-volume --region {} --volume-type gp2 --snapshot-id {} --availability-zone {}'.format(volumetype,snapshotid,avazone)
output = sp.getoutput(cmd)
print(output)
