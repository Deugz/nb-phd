#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

secs = int(input('enter time in seconds : '))
while secs:
    mins, sec = divmod(secs, 60)
    timef = '{:02d}:{:02d}'.format(mins,sec)
    print(timef,end="\r")
    time.sleep(1)
    secs-=1

print()
print("Done!")


# In[ ]:




