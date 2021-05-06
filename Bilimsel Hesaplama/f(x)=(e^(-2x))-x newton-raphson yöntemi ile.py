#!/usr/bin/env python
# coding: utf-8

# In[2]:


from math import e

def f(x):
    return(e**(-2*x)-x)

def fi(x):
    return(-2*e**(-2*x)-1)

def hata(x1,x2):
    return(abs((x1-x2)/x1))

x1 = int(input("tahmin girin: "))

for i in range(10):
    x2 = x1 - f(x1)/fi(x1)
    print(x1,x2,hata(x1,x2))
    x1 = x2


# In[ ]:





# In[ ]:




