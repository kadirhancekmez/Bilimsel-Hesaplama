#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f(x,y):
    return(x**2+x*y-10)

def g(x,y):
    return(y+3*x*y**2-57)

def fx(x,y):
    return(2*x+y)
def fy(x,y):
    return(x)
def gx(x,y):
    return(3*y**2)
def gy(x,y):
    return(1+6*x*y)

xi = float(input("başlangıç tahmini girin: "))
yi = float(input("başlangıç tahmini girin: "))

for i in range(5):
    xi -= (f(xi,yi)*gy(xi,yi)-g(xi,yi)*fy(xi,yi))/(fx(xi,yi)*gy(xi,yi)-fy(xi,yi)*gx(xi,yi))
    yi += (f(xi,yi)*gx(xi,yi)-g(xi,yi)*fx(xi,yi))/(fx(xi,yi)*gy(xi,yi)-fy(xi,yi)*gx(xi,yi))
    print(xi,yi)


# In[ ]:




