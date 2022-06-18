#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_excel('Telco-Customer-Churn.xlsx')
data.head()


# In[3]:


#check null values
data.isna().sum()


# # compare churn count with respect to gender

# In[4]:


data['gender'].value_counts()


# In[5]:


plt.figure(figsize=(6,6))
sns.countplot(x='gender',hue='Churn',data=data)
plt.title('Gender vs. Churn Count')
plt.tight_layout()


# # find out how many female citizens are there in the dataset

# In[6]:


df=data[(data['gender']=='Female')&(data['SeniorCitizen']==1.0)]
df.count()


# There are 568 female senior citizens 

# # Compare 'tenure' with 'Total Charges'

# In[7]:


plt.figure(figsize=(10,6))
sns.lineplot(x='tenure',y='TotalCharges',data=data)
plt.title('Tenure vs.Total Charges',size=15)


# # Find out which contract is preferred by the senior citizen

# In[8]:


df1=data[data['SeniorCitizen']==1.0]
df1


# In[9]:


sns.countplot(x='Contract',data=df1)
plt.title('contract preffered by seniorcitizens',size=15)
plt.tight_layout()


# most of the senior citizens preffer month month contract

# # Comment on your finds on payment method

# In[10]:


data['PaymentMethod'].value_counts()


# In[11]:


plt.figure(figsize=(8,6))
sns.countplot(x='PaymentMethod',data=data)
plt.title('payment method classification')
plt.xticks(rotation=90)


# In[12]:


#payment method vs gender
sns.countplot(x='gender',data=data,hue='PaymentMethod')
plt.legend(loc=(1.02,0))


# In[13]:


#payment method vs senior citizen
sns.countplot(x='SeniorCitizen',data=data,hue='PaymentMethod')
plt.legend(loc=(1.02,0))


# It is seen that Electronic check is the most preffered payment
# method for both senior citizen as well as non senior citizen.

# In[ ]:




