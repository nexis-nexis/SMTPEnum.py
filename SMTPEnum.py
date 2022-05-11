#!/usr/bin/python

# The socket module in pythin is an interface to the Berkeley sockets API.
import socket
# socket module is used to connect to the server
import sys

import subprocess

# date and time 

from datetime import datetime

if len(sys.argv) != 2:
     print "Usage: smtp_vrfy.py <usernames file>"
     sys.exit(0)

user_file = open(sys.argv[1])
names = user_file.read().splitlines()

#Create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defining our socket

# Connect to the server

connect=s.connect(('10.10.10.7',25))

# Receive banner

banner=s.recv(1024)

print banner

#Check the date and time the scan was started
t1 = datetime.now()

for name in names:

    #VRFY a user

    s.send('VRFY ' + name + '\r\n')

    result=s.recv(1024)

    print result

user_file.close()


#Checking time again
t2 = datetime.now()

#Calculate the difference in time to now how long the scan took
total = t2 - t1

#Printing the information on the screen
print 'Scanning Completed in in ', total

# Close the socket

s.close()


