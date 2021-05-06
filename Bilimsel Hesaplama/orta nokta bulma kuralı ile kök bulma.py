#!/usr/bin/env python
# coding: utf-8

# In[5]:


def f(x):
    return (x**2-3*x-4)


# In[6]:


x1 = int(input("ilk tahmini giriniz: "))
x2 = int(input("ilkikinci tahmini giriniz: "))


# In[7]:


if(f(x1)*f(x2) == 0):
    print("tahminlerinizden biri köktür")
elif(f(x1)*f(x2) > 0):
    print("bu aralıkta bir kök yoktur.")
else:
    for i in range(10):
        xr=(x1+x2)/2
        if(f(xr)==0):
            print("denklemin kökü ",xr)
            break
        elif(f(x1)*f(xr)<0):
            x2=xr
        else:
            x1=xr
        print(xr)


# In[ ]:




