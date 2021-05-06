#!/usr/bin/env python
# coding: utf-8

# In[2]:



from math import factorial
from decimal import *
getcontext().prec = 42
e = 1

for n in range(1,70):
    e += Decimal(1/factorial(n))
print(n, e)


# In[ ]:





# In[ ]:




