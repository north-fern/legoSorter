#!/usr/bin/env python
# coding: utf-8

# In[2]:


import serial
import cv2
#from PIL import Image
import time

s = serial.Serial("/dev/serial0", 9600, timeout = 200)

# while True:
#     try:
#         print("Writing Message")
#         s.write("hi".encode())
#         time.sleep(.5)
# #         message = s.readline()
#         #print(type(message))
# #         mes = message.decode('utf-8')
#         #print("The Message is: " , mes)
#     except:
#         print("I CANNOT SEND THE DATA PLZ HELP")
#         pass
#        # message = s.readline()
#        # print("FAILED MESSAGE: " , message)
#        # print(type(message))


# In[3]:


def newImage():
    image = cv2.VideoCapture(0)
    r,f = image.read()
    image.release()
    return f


# In[4]:


def splitVectorsToHists(ary):
    z1 = cv2.calcHist([ary[200:500, 200:500, :]], [0], None, [256], [0,256])
    z2 = cv2.calcHist([ary[200:500, 200:500, :]], [1], None, [256], [0,256])
    z3 = cv2.calcHist([ary[200:500, 200:500, :]], [2], None, [256], [0,256])
    return z1, z2, z3


# In[5]:


def colorThreshold(c1, c2, c3):
    z1t = 0
    z2t = 0
    z3t= 0

    for i in range(240, 256):
        z1t += c1[i]
        z2t+= c2[i]
        z3t += c3[i]

    return z1t, z2t, z3t


# In[6]:


def decideColor(c1t, c2t, c3t):
    if c3t - c1t - c2t > 0:
        print("IMAGE MOSTLY RED")
        return 2
    else:
        print("NOT RED")
        return 0


# In[ ]:


i = 0
while i < 50:
    picture =  newImage()
    b, g, r = splitVectorsToHists(picture)
    bt, gt, rt,  = colorThreshold(b, g, r)
    ans = decideColor(bt, gt, rt)
    print(ans)
    time.sleep(.5)
    i += 1


# In[ ]:


while True:
    picture =  newImage()
    b, g, r = splitVectorsToHists(picture)
    bt, gt, rt,  = colorThreshold(b, g, r)
    ans = decideColor(bt, gt, rt)
    print(ans)
    time.sleep(.1)
    s.write(str(ans).encode())


# In[ ]:




