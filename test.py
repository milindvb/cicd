#!/usr/bin/python

import sys
import os
import subprocess
import io
import re
import time


scdir = "/home/cmust_user/current/script"
homedir = "/home/cmust_user"
bindir = "/home/cmust_user/bin"

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

os.chdir(scdir)

logfile = sys.argv[1]
logcmd = "/home/cmust_user/current/script/logwindow "+logfile+" > /dev/null 2>&1 &"
print "logcmd is =", logcmd

#process = subprocess.Popen('nohup /home/cmust_user/current/script/logwindow results1.log', shell = True)
#process = subprocess.Popen(['logwindow', 'results1.log', '&'])
#process = subprocess.Popen(' /home/cmust_user/current/script/logwindow results1.log > /dev/null 2>&1 &', shell = True)
process = subprocess.Popen(logcmd, shell = True)


print "process ID========", process.pid+1

sys.exit()

#file = open("results1.log","r")

#for line in file:
#   if "SWERR" in line:
#      print "Error found"
#      process.terminate()

# testing
# from branch dev
