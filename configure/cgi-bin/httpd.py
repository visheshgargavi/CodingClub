#!/usr/bin/python3
print("content-text: text/plain")
print()

import subprocess as sp
import os
import cgi

print("NOTE: Kindly make sure yum is configured before configuring webserver")
field = cgi.FieldStorage()

cmd = "sudo yum install httpd -y"
output1 = sp.getoutput(cmd)
print("\n")
print(output1)

cmd1 ="cp -rvf /var/www/cgi-bin/index.html /var/www/html/auto.html"
output2 = sp.getoutput(cmd1)
print(output2)

cmd2 ="sudo systemctl stop firewalld"
output3 = sp.getoutput(cmd2)
print(output3)

cmd3 ="sudo systemctl start httpd"

output4 = sp.getoutput(cmd3)
print(output4)



