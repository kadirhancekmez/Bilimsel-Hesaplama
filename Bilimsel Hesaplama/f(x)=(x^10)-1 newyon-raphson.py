#!/usr/bin/env python
# coding: utf-8

# In[2]:


def f(x):
    return(x**10-1)

def fi(x):
    return(10*x**9)

def hata(x1,x2):
    return(abs((x1-x2)/x1))

x1 = int(input("tahmin girin: "))
h = 1

while(h>(10**(-10))):
    x2 = x1 - f(x1)/fi(x1)
    h = hata(x1,x2)
    print(x1,h)
    x1 = x2


# In[ ]:




