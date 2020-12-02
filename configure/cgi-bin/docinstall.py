#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import os
import cgi

field = cgi.FieldStorage()

cmd1 = "sudo sudo yum config-manager --add-repo=https://download.docker.com/linux/centos/7/x86_64/stable/"
output1 = sp.getoutput(cmd1)

cmd2 = "sudo dnf install docker-ce --nobest -y"
output2 = sp.getoutput(cmd2)

cmd3 = "sudo systemctl start docker"
output3 = sp.getoutput(cmd3)

cmd4 = "sudo systemctl status docker"
output4 = sp.getoutput(cmd4)

print(output2)
print(output4)
