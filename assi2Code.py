#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
SuperMarket = pd.read_csv(r'C:\Users\alaau\OneDrive\Desktop\Assignment Two\supermarket_sales.csv')   
# 1
SuperMarket['Date'] = pd.to_datetime(SuperMarket['Date'])
SuperMarket.sort_values(by=["Date"], inplace=True)
plt.figure(figsize = (15,8))
sns.lineplot(x= SuperMarket['Date'],y=SuperMarket['gross income'] )
plt.title('Gross income over time', fontsize=16)
plt.show()


# In[22]:


# 2
plt.figure(figsize = (15,5))
SuperMarket.groupby('Date').sum()['Total'].plot()
plt.xticks(rotation=45)
plt.title('Sales over time', fontsize=16)
plt.ylabel('Sales', fontsize=16)


# In[9]:


# 3
SuperMarket.groupby('Branch').sum()['Total'].plot.bar()
plt.xticks(rotation=0)
plt.title('Branshes sales', fontsize=16)
plt.ylabel('Sales', fontsize=16)
print(SuperMarket.groupby('Branch').sum()['Total'])


# In[21]:


# 4
plt.figure(figsize = (15,8))
plt.style.use('classic')
ax = sns.countplot(x = "Customer type", hue = "Branch", data = SuperMarket, palette= "rocket_r")
ax.set_title(label = "Customer type in different branch", fontsize = 25)
ax.set_xlabel(xlabel = "Branches", fontsize = 16)
ax.set_ylabel(ylabel = "Number of Customer", fontsize = 16)


# In[13]:


# 5
SuperMarket.groupby('City').sum()['gross income'].plot.bar()
plt.xticks(rotation=0)
plt.title('Relationship between gross income and city', fontsize=16)
plt.ylabel('Gross income', fontsize=16)
print(SuperMarket.groupby('City').sum()['gross income'])


# In[14]:


# 6
SuperMarket.groupby('Branch').mean()['Rating'].plot.bar()
plt.xticks(rotation=0)
plt.title('Average rate of branches', fontsize=16)
plt.ylabel('Avg rate', fontsize=16)
print(SuperMarket.groupby('Branch').mean()['Rating'])


# In[15]:


# 7
SuperMarket.groupby('Gender').mean()['Rating'].plot.bar()
plt.xticks(rotation=0)
plt.title('Relationship between customer gender and rating', fontsize=16)
plt.ylabel('Avg rate', fontsize=16)
print(SuperMarket.groupby('Gender').mean()['Rating'])


# In[16]:


# 8
values = SuperMarket['Gender'].value_counts()
labels= SuperMarket['Gender'].unique().tolist()
colors=['Pink','lightBlue']
plt.pie(values ,labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
plt.title('Customers gender distribution')
plt.show()


# In[17]:


# 9
values = SuperMarket['Payment'].value_counts()
labels= SuperMarket['Payment'].unique().tolist()
colors=['yellow','lightgreen','lightblue']
plt.pie(values ,labels=labels, colors=colors, startangle=90, autopct='%1.1f%%',shadow=True,explode=(0.1, 0.0, 0.0,))
plt.title('supermarket payment preferences')
plt.show()
print("From the chart, Ewallet is the most popular payment method")


# In[18]:


#10
plt.figure(figsize = (15,8))
ax = sns.countplot(x = "Payment", hue = "Gender", data = SuperMarket, palette= "rocket_r")
ax.set_title(label = "payment type usage across the genders", fontsize = 25)
ax.set_xlabel(xlabel = "Payment method", fontsize = 16)
ax.set_ylabel(ylabel = "Number of users", fontsize = 16)


# In[19]:


#11
SuperMarket.groupby('Product line').sum()['Total'].plot.bar()
plt.xticks(rotation=45)
plt.title('Sales per product', fontsize=16)
plt.ylabel('Sales', fontsize=16)
print(SuperMarket.groupby('Product line').sum()['Total'])


# In[ ]:




