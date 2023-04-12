#!/usr/bin/env python
# coding: utf-8

# In[5]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[6]:


import statistics


# In[3]:


df=sns.load_dataset('iris')


# In[4]:


df.head()


# In[18]:


np.mean(df['sepal_width'])


# In[20]:


np.median(df['sepal_width'])


# In[21]:


statistics.mode(df['sepal_width'])


# In[24]:


sns.boxplot(df['sepal_width'])


# In[27]:


sns.histplot(df['sepal_width'],kde=True)


# In[32]:


np.percentile(df['sepal_width'],[25,75])


# In[43]:


dataset=[22,23,25,26,21,20,19,23,26]
q1,q3=np.percentile(df['sepal_width'],[25,75])
print(q1,q3)


# In[44]:


iqr=q3-q1
iqr


# In[47]:


Lower_fence=q1-(1.5*iqr)
Higher_fence=q1+(1.5*iqr)
print(Lower_fence)
print(Higher_fence)


# In[5]:


df.corr()


# In[6]:


sns.pairplot(df)


# In[11]:


data=[11,12,14,15,18,102,15,17,16,13,108,15,19,11,12]


# In[16]:


outliers=[]
def detect_outliers(data):
    threshold=1
    mean=np.mean(data)
    std=np.std(data)
    
    for i in data:
        z_score=(i-mean)/std
        if np.abs(z_score)>threshold:
            outliers.append(i)
            
    return outliers
    


# In[17]:


detect_outliers(data)


# In[18]:


#IQR
data=sorted(data)
data


# In[22]:


q1,q3=np.percentile(dataset,[25,75])
print(q1,q3)


# In[24]:


iqr=q3-q1
print(iqr)


# In[26]:


lower_fence=q1-1.5*(iqr)
higher_fence=q3+1.5*(iqr)
print(lower_fence)
print(higher_fence)


# In[ ]:




