#!/usr/bin/env python
# coding: utf-8

# In[2]:


def f(x):
    return(x**5-7*x**4+18*x**3-22*x**2+13*x-3)
def fi(x):
    return(5*x**4-28*x**3+54*x**2-44*x+13)

x1 = float(input("baslangic tahmini girin: "))

for i in range(30):
    x1 = x1 - f(x1)/fi(x1)
    print(x1)


# In[ ]:




