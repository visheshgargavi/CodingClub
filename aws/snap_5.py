#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()
snapshotid = field.getvalue('sid')

cmd = 'sudo /usr/local/bin/aws ec2 delete-snapshot --snapshot-id {}'.format(snapshotid)
output = sp.getoutput(cmd)
print(output)
