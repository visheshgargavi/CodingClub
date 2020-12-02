#!/usr/bin/python3
print("content-type: text/plain")
print()

import os
import subprocess as sp
import cgi

field = cgi.FieldStorage()

j_dir = field.getvalue("j")
h_dir = field.getvalue("h")
n_dir = field.getvalue("n")
ip = field.getvalue("i")
port = field.getvalue("p")
print("\t\t\t\t\t Namenode Configuration")
cmd = "sudo rm -rf /var/www/cgi-bin/hdfs-site.xml /var/www/cgi-bin/core-site.xml"
o2 = sp.getstatusoutput(cmd)
c2 = "sudo touch /var/www/cgi-bin/core-site.xml /var/www/cgi-bin/hdfs-site.xml"
oo2 = sp.getoutput(c2)
c3 = "sudo chmod 777 *"
oo3 = sp.getoutput(c3)
cmd0 = "sudo cp -rf hp.xml /var/www/cgi-bin/core-site.xml"
o1 = sp.getstatusoutput(cmd0)
c1 = "sudo cp -rf cp.xml /var/www/cgi-bin/hdfs-site.xml"
oo1 = sp.getstatusoutput(c1)
cmd1 = "sudo rpm -i {}/jdk-8u171-linux-x64.rpm".format(j_dir)
output1 = sp.getoutput(cmd1)
print('\n')
print(output1)

cmd2 = "sudo rpm -i {}/hadoop-1.2.1-1.x86_64.rpm --force".format(h_dir)
output2 = sp.getoutput(cmd2)
print(output2)

cmd3 = 'sudo echo \<configuration\> >> /var/www/cgi-bin/hdfs-site.xml'
o3 = sp.getstatusoutput(cmd3)
cmd4 = 'sudo echo \<property\> >> /var/www/cgi-bin/hdfs-site.xml'
o4 = sp.getstatusoutput(cmd4)
cmd5 = 'sudo echo <name>dfs.name.dir</name> >> /var/www/cgi-bin/hdfs-site.xml'
o5 = sp.getstatusoutput(cmd5)
cmd6 = 'sudo echo "<value>{}</value>" >> /var/www/cgi-bin/hdfs-site.xml'.format(n_dir)
o6 = sp.getstatusoutput(cmd6)
cmd7 = 'sudo echo "</property>" >> /var/www/cgi-bin/hdfs-site.xml'
o7 = sp.getstatusoutput(cmd7)
cmd8 = 'sudo echo "</configuration>" >> /var/www/cgi-bin/hdfs-site.xml'
o8 = sp.getstatusoutput(cmd8)
cmd9 = "sudo chmod 777 /etc/hadoop/"
o9 = sp.getstatusoutput(cmd9)
cmd10 = "sudo cp -rf /var/www/cgi-bin/hdfs-site.xml /etc/hadoop/hdfs-site.xml"
o10 = sp.getstatusoutput(cmd10)
cmd11 = "sudo cat /etc/hadoop/hdfs-site.xml"
output3 = sp.getoutput(cmd11)
print('Content of hdfs-site.xml')
print(output3)
print('\n')


cmd13 = 'sudo echo \<configuration\> >> /var/www/cgi-bin/core-site.xml'
o13 = sp.getstatusoutput(cmd13)
cmd14 = 'sudo echo \<property\> >> /var/www/cgi-bin/core-site.xml'
o14 = sp.getstatusoutput(cmd14)
cmd15 = 'sudo echo \<name\>fs.default.name\<\/name\> >> /var/www/cgi-bin/core-site.xml'
o15 = sp.getstatusoutput(cmd15)
cmd16 = "sudo echo \<value\>hdfs://{}:{}\<\/value\> >> /var/www/cgi-bin/core-site.xml".format(ip,port)
o16 = sp.getstatusoutput(cmd16)
cmd17 = "sudo echo \<\/property\> >> /var/www/cgi-bin/core-site.xml"
o17 = sp.getstatusoutput(cmd17)
cmd18 = "sudo echo \<\/configuration\> >> /var/www/cgi-bin/core-site.xml"
o18 = sp.getstatusoutput(cmd18)
cmd20 = "sudo cp -rf /var/www/cgi-bin/core-site.xml /etc/hadoop/core-site.xml"
o20 = sp.getstatusoutput(cmd20)
cmd21 = "sudo cat /etc/hadoop/core-site.xml"
output4 = sp.getoutput(cmd21)
print('Content of core-site.xml')
print(output4)
print('\n')

cmd22 = "sudo mkdir {}".format(n_dir)
output5 = sp.getstatusoutput(cmd22)
if output5[0]==0:
  print("\n {} create successfully".format(n_dir))
else:
  print("\n {} already exist".format(n_dir))

cmd23 = "sudo echo Y | hadoop namenode -format"
output6 = sp.getoutput(cmd23)
print(output6)
print('\n')

cmd25 = "sudo hadoop-daemon.sh start namenode"
output8 = sp.getoutput(cmd25)
print(output8)
print('\n')

cmd24 = "sudo jps"
output7 = sp.getoutput(cmd24)
print(output7)
print('\n')


