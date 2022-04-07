#!/usr/bin/env python
# coding: utf-8

# In[8]:


import socket


# In[4]:


import threading


# In[ ]:


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# In[ ]:


port = 5000
# binding with any ip addres
ip=""


# In[ ]:


# binding with a specific ip @
# ip="192.168.56.101"

s.bind((ip, port))
s.listen()

csession, addr = s.accept()

print(addr)


# In[ ]:


#serial client connections manully
#client 1
#csessionA, addr = s.accept()
#print(addr)

#csessionA.send(b" <<-----------------  This is from server")
# param of recv is the size of data in Byte
#data=csessionA.recv(100)
#print(data)


# In[ ]:


#client 2
#csession2, addr = s.accept()
print(addr)
#csession2.send(b"<<-----------------  From the server...")
# param of recv is the size of data in Byte
#data=csession2.recv(100)
#print(data)


# In[ ]:


#serial client connections by looping infinitely
#Each current client has to finish its operation and release the server for the next client to connect and so on
#while True:
   #client 1
#    csession, addr = s.accept()
#    print(addr)
#    csession.send(b" <<-----------------  This is from server")
    # param of recv is the size of data in Byte
#    data=csession.recv(100)
#    print(data)


# In[7]:


def serverConnClient():
    #server accepts connetion
    #csession, addr = s.accept()  commented because used in multithreadung part
    print(addr)
    csession.send(b" <<-----------------  This is from server")
    # param of recv is the size of data in Byte
    data=csession.recv(100)
    print(data)


# In[ ]:


#multithreading
while True:
    #server accepts connetion
    csession, addr = s.accept()
    #define a threat
    T1 = threading.Thread(target=serverConnClient, args=(csession, addr))
    #start the threat
    T1.start()

