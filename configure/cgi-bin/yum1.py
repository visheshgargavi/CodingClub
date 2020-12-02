#!/usr/bin/python3
print("content-type: text/plain")
print()

import cgi
import subprocess as sp
print("\t\t\t\t\t\t YUM CONFIGURATION ")
field=cgi.FieldStorage()
dir=field.getvalue("t")
cmd10 = "sudo rm -rfv /etc/yum.repos.d/dvd.repo"
sp.getstatusoutput(cmd10)
cmd= "sudo mkdir {}".format(dir)
output1=sp.getstatusoutput(cmd)
#print(output1,end="")
if output1[0]==0:
  print("\n {} create successfully".format(dir))
else:
  print("\n {} already exist".format(dir))

cmd1 = "sudo mount /dev/cdrom {}".format(dir)
output2 = sp.getstatusoutput(cmd1)
if output2[0]==0:
    print('\n')
    print("\n /dev/cdrom mounted successfully")
else:
    print('\n')
    print("\n sorry /dev/cdrom is already mounted kindly check your instance")

sp.getstatusoutput("sudo touch /etc/yum.repos.d/dvd.repo")
sp.getstatusoutput("sudo chmod 777 /etc/yum.repos.d/dvd.repo")
cmd3 = "sudo echo [dvd] >> /etc/yum.repos.d/dvd.repo"
sp.getstatusoutput(cmd3)
cmd5 = "sudo echo baseurl\=file://{}\/BaseOS >> /etc/yum.repos.d/dvd.repo".format(dir)
sp.getstatusoutput(cmd5)
cmd6 = "sudo echo gpgcheck\=0 >> /etc/yum.repos.d/dvd.repo"
sp.getstatusoutput(cmd6)
cmd7 = "sudo echo [dvd1] >> /etc/yum.repos.d/dvd.repo"
sp.getstatusoutput(cmd7)
cmd8 = "sudo echo baseurl\=file://{}\/AppStream >> /etc/yum.repos.d/dvd.repo".format(dir)
sp.getstatusoutput(cmd8)
cmd9 = "sudo echo gpgcheck\=0 >> /etc/yum.repos.d/dvd.repo"
sp.getstatusoutput(cmd9)
cmd11 = "sudo cat /etc/yum.repos.d/dvd.repo"
output3 = sp.getoutput(cmd11)

print(output3)
cmd12 = "sudo yum clean all"
output4 = sp.getoutput(cmd12)
print('\n')
print(output4)
print("\t\t\t\t\tYUM CONFIGURED SUCCESSFULLY!! ")
#cmd13 = "sudo yum repolist"
#output5 = sp.getoutput(cmd13)
#print('\n')
#print(output5)
