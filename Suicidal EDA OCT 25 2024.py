#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dataset about suicidal rates 1985 to 2016 
# October 2024

# Goal to identify which gender has most suicidal case and which year and which age 

import pandas as pd
import numpy as np


# In[79]:


#load the file

df=pd.read_csv('master.csv')
df


# In[80]:


# Data exploration
df.head()
df.info()
df.describe()


# In[81]:


#checking for missing values
df.isnull().sum()


# In[82]:


#Drop missing data

df.dropna(inplace=True)
df


# In[83]:


df 


# In[84]:


#check for any duplicate rows in the dataset

df.duplicated().sum()
 


# In[85]:



#Number of countries in the dataset
df.country.unique()


# In[86]:


#Number of countries in the dataset
len(df.country.unique())


# In[87]:


#Exploratory Data Analysis

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('whitegrid')




# In[88]:


#Analysing suicide cases generally on the basis of sex by creating two seperate Dataframes (one for male the other for female)
df_male = df[df.sex == 'male']
df_female = df[df.sex == 'female']

df_male['age'].dtype


# In[89]:


#We now check if there are any null values present in the dataset
df.isnull().sum() 


# In[90]:


plt.figure(figsize = (20,8))
sns.lineplot(x=df_male.year, y=df_male.suicides_no,ci=None)
sns.lineplot(x=df_female.year, y=df_female.suicides_no,ci=None)
plt.legend(["Male",'Female'])
plt.show() 


# In[ ]:


#Conclusion of this plot Male suicidal rate is more
        


# In[118]:


# plotting male age and number of suicidal

df_male_grouped=df_male.groupby(["year","age"])['suicides_no'].sum()
df_male_grouped.head(20)


# In[119]:


# Find the age group with the maximum male suicides

max_suicides_by_age = df_male_grouped.idxmax()
max_suicides_value = df_male_grouped.max()
print("Age Group with Most Suicides:", max_suicides_by_age)
print("Number of Suicides in that Age Group:", max_suicides_value)


# In[110]:


max_suicides_by_age = df_male_grouped.groupby('age').max()

# Plotting a bar chart
plt.figure(figsize=(12, 6))
max_suicides_by_age.plot(kind='bar', color='skyblue')
plt.title('Maximum Suicides by Age Group (Males)')
plt.xlabel('Age Group')
plt.ylabel('Number of Suicides')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Optional: Add a grid for easier interpretation
plt.show()


# In[111]:


#Conclusion

#Age group 35-54 range has higher sucidal cases 


# In[ ]:




