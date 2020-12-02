#!/usr/bin/python3
print("content-text: text/html")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
cont = field.getvalue("x")

cmd1 = "sudo rm -rf /var/www/cgi-bin/docker/Dockerfile"
out1 = sp.getoutput(cmd1)
cmd2 = "sudo touch /var/www/cgi-bin/docker/Dockerfile"
out2 = sp.getoutput(cmd2)
cmd3 = "sudo chmod 777 /var/www/cgi-bin/docker/Dockerfile"
out3 = sp.getoutput(cmd3)
cmd4 = 'sudo echo "{}" >> /var/www/cgi-bin/docker/Dockerfile'.format(cont)
out4 = sp.getoutput(cmd4)
cmd5 = "sudo cat /var/www/cgi-bin/docker/Dockerfile"
output = sp.getoutput(cmd5)
print(output)



