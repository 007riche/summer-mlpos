#!/usr/bin/env python
# coding: utf-8

# In[1]:


# WE can load the trained model as such 


# In[2]:


# lib's importation
import joblib


# In[8]:


# model extraction or loading
# Any extension works
# usage of pk1 extension is a best practice

brain = joblib.load('salaryPredict.pk1Test')


# In[9]:


# test
brain.predict([[5]])


# In[ ]:


# successful Test

