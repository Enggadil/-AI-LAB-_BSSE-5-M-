#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
data=pd.read_csv(r'iris_data_2a.csv')
print(data.head())


# In[2]:


x=data.drop('species','columns')
y=data['species']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
scaler=StandardScaler()
scaler.fit(x_train)


# In[3]:


x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)


# In[4]:


print(x_train)


# In[5]:


print(x_test)


# In[6]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
result= regressor.predict(x_test)
print("Result:\n",result)


# In[7]:


# Evaluating Model's Performance
from sklearn.metrics import mean_absolute_error,mean_squared_error
print('Mean Absolute Error:', mean_absolute_error(y_test, result))
print('Mean Squared Error:', mean_squared_error(y_test, result))
print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, result)))


# In[ ]:




