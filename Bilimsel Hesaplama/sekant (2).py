#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f(x):
    return(x**2-2*x-8)

x1 = float(input("başlangıç tahmini girin: "))
x3 = float(input("başlangıç tahmini girin: "))

while(f(x3)!=f(x1)):       #2. tahmının goruntusu ılk tahmınden farklı oldugu surece sunu yap
    x2 = x1 - (f(x1)*(x3-x1))/(f(x3)-f(x1))
    print(x3)
    x1, x3 = x3, x2


# In[ ]:




