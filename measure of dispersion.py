#!/usr/bin/env python
# coding: utf-8

# In[3]:


#measure dispersion
##variance and standard deviation


# In[4]:


ages=[23,24,25,26,76,54,54,32,53]


# In[5]:


import numpy as np


# In[7]:


mean=np.mean(ages)


# In[8]:


mean


# In[9]:


var=np.var(ages)


# In[10]:


var


# In[12]:


std=np.std(ages)


# In[13]:


std


# In[15]:


import pandas as pd


# In[16]:


data=[[10,12,13],[29,24,25],[24,30,29]]


# In[17]:


data


# In[20]:


df=pd.DataFrame(data)


# In[21]:


df


# In[22]:


df.var(axis=0)


# In[23]:


df.var(axis=1)


# In[25]:


df.var()
#by default axis=0


# In[26]:


df.std()


# In[27]:


df.std(axis=1)


# In[ ]:




