#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import e

x = 0
hata = 1

while(hata>0.0001):
    x1 = e**(-2*x)
    hata = abs((x1-x)/x1)
    x = x1
    print(x, hata)


# In[ ]:




