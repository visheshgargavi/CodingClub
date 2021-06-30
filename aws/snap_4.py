#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
volumetype = field.getvalue('vt')
region = field.getvalue('r')
snapshotid = field.getvalue('sid')
iops = field.getvalue('iop')
avazone = field.getvalue('az')  

cmd = 'sudo /usr/local/bin/aws ec2 create-volume --region {} --volume-type {} --iops {} --snapshot-id {} --availability-zone {}'.format(region,volumetype,iop,snapshotid,ava-zone) 

output = sp.getoutput(cmd)
print(output)
