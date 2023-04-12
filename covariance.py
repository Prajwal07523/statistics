#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[7]:


df=sns.load_dataset('healthexp')
df.head()


# In[8]:


import numpy as np


# In[9]:


df.cov()


# In[10]:


df.corr(method='spearman')


# In[11]:


#pearson
df.corr(method='pearson')


# In[ ]:




