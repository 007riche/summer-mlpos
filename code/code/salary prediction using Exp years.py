#!/usr/bin/env python
# coding: utf-8

# In[1]:


# lib allowing us to load custom data in notebook 
import pandas


# In[2]:


#load datas form salary into variable named 'dat'
dat = pandas.read_csv('salary.csv')


# In[3]:


#display dat
dat
#col names are displayed below


# In[4]:


#retrieve exp column
experience= dat['YearsExperience']


# In[5]:


experience.shape


# In[6]:


type(experience)


# In[7]:


## DUE TO CONVERSION STEP, ONLY ONE EXECUTION OF THIS CELL IS CORRECT

#convert the variable into a numpy type variable if only the variable is different type

# Nice conversion step 
# experienceVal = dat['YearsExperience'].values  ## ==> give a numpy
# experienceVal = experienceVal.reshape(-1, 1)

#here as experience var is the retrieved form of values in dat's yearsExp column, it has no more values attribute which 
#when retrieved is a pandas object

#display the new type
# type(experienceVal)


#reshaping the variable
experience= experience.values  # ==> numpy array

## IMPORTANT NOTE: conversion is made only once. A use case of error is when the conversion and reshaping 
# are kept in single cell and the cell is executed many times because CONVERSION IS DONE ONLY ONCE, SO TRYING TO EXECUTE 
# THE CELL CONTAINING CONVERSION MAY LEAD TO EXECUTION ERROR 
## ONE WAY TO AVOID SUCH KIND OF ERROR IS TO USE DIFFERENT VARIABLES INSTEAD OF USING SAME VAR (RE-ASSIGNMENT ) DURING 
# CONVERSION OF TYPE
# Eg: NewExperienceVar = experience.values 


# In[8]:


experience= experience.reshape(30, 1)
type(experience)

#display the temp final shape (in terme of dimensions of the object i.e. 1D, 2D, 3D, etc...)
experience.shape


# In[9]:


#retrieve salary column
salary =dat['Salary']


# In[10]:


#display experience var
experience


# In[11]:


#salary
salary


# In[12]:


#importation of the LRegr function
from sklearn.linear_model import LinearRegression


# In[13]:


# LRegr initialization
# the linear regression formula is Y=aX + Cst
model = LinearRegression()


# In[14]:


# training
# param is a 2D array [x][y]
# x: input
# y: output (predicted value)
model.fit(experience, salary)


# In[15]:


#display the coef of the final trained model, 'a' in "Y=aX + Cst"
model.coef_


# In[16]:


#example of prediction
#note on param nature, it is a 2D array,

model.predict([[2.5]])


# In[17]:


## To save the trained model we use one function in a lib provided for that
## lib name 'joblib'
#importation
import joblib


# In[18]:


## backup creation
## typical extension used is pk1 (theoritcally, we can use any extnsion)
# this file is also known as weight file

joblib.dump(model, 'salaryPredict.pk1')
joblib.dump(model, 'salaryPredict.pk1Test')


# In[ ]:




