#!/usr/bin/env python
# coding: utf-8

# In[1]:



def f(x):
    return(x**2-3*x-4)

def fi(x):
    return(2*x-3)

def hata(x1,x2):
    return(abs((x1-x2)/x1))

x1 = int(input("tahmin girin: "))

for i in range(10):
    x2 = x1 - f(x1)/fi(x1)
    print(x1,x2,hata(x1,x2))
    x1 = x2


# In[ ]:




