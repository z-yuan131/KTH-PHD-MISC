#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
from math import pi


# In[33]:


### calculate the boundary layer mesh which meets y+ requirement
p = 1.05
ds_design = 0.0004
layer = 50
T = 0.2
tol = 0.00001
ds = 100
k = 0
while(abs(ds - ds_design) > tol):
    ds_last = ds
    if (ds < ds_design):
        layer = layer - 1
    else:
        layer = layer + 1
    
    temp = 0
    for i in range(layer):
        temp += p**(i)
    ds = T/temp
    
    k += 1
    
    if ds_last - ds_design > 0 and ds - ds_design < 0 and k > 1:
        print(ds)
        print(layer)
        break
    
print('ds = '+str(ds)+'\n')
print('layer = '+str(layer)+'\n')


# In[34]:


### calculate the boundary layer mesh which meets y+ requirement



    
temp = 0
for i in range(layer):
    temp += p**(i)
ds_validation = T/temp

if ds == ds_validation:
    print('Validation approved!')
else:
    print('calculation wrong!')


# In[ ]:




