#!/usr/bin/env python
# coding: utf-8

# In[1]:


##measure centarl tendency


# In[12]:


age=[12,13,14,15,16,12,28]


# In[4]:


import numpy as np
np.mean(age)


# In[5]:


weights=[67,58,93,67,88,94,50]
np.mean(weights)


# In[7]:


weights1=[67,58,93,67,88,94,50,1000]
np.mean(weights1)
#1000 is the outlier


# In[8]:


np.median(weights1)

