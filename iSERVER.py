#!usr/bin/env python 

#Do not mess my code
#For those who do not like messy code for their Chat Server hear is simple code 

from socket import *
import random

s = socket(AF_INET, SOCK-STREAM)    #If you use from socket import * Ther is no need for socket.socket(socket.AF_INET,)

HOST = '' #it is going to take HOST ip automatically
PORT = random.randit(1025, 60000) #Windows 7 will not allow you to use the same port TWICE so randomed my port numbers
BUFSIZ = 1024 #Y so much data i dont mean to be lyk TWITTER but TCP splits DATA
ADDR = (HOST, PORT)  #I wont need to use the whole tuple thank you VARIABLES

s.bind(ADDR)
s.listen(5)

while True:
    print '....waiting for connection...'
    s, addr = s.accept()
    print "Connected to " addr
    print 'The name is probably', gethostname()
    
    while True:
        data = recv(BUFSIZ)
        print data
        
        #Finish the rest on your own
