#!/usr/bin/env python
# coding: utf-8

# ## IMDB MOVIE DATA ANALYSIS
# PREPARED BY : ISHAN NAUTIYAL \
# DATE : 13/09/2023  \
# DATASET : KAGGLE 

# In[1]:


#import important libraries 
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 


# In[2]:


# read the data from the dataset 
df1 = pd.read_csv("C:\\Users\\ishan\\datasets\\IMDB-Movie-Data.csv")


# In[3]:


# convert to pandas data frame 


# In[5]:


df1 = pd.DataFrame(df1)


# ## FIRST  10 AND LAST 10 ROWS 

# In[6]:


df1.head(10)


# In[7]:


df1.tail(10)


# ## SHAPE OF THE DATASET 
# 

# In[8]:


data = df1.shape


# In[9]:


print(f"the number of rows are {data[0]} and number of column are {data[1]}")


# ## INFORMATION ABOUT DATASET 

# In[10]:


df1.info


# ## check for the null values write code and visualize it simultaneously

# In[11]:


df1.isnull().sum()


# In[12]:


sns.heatmap(df1.isnull())


# In[13]:


per_null = df1.isnull().sum()*100/len(df1)


# In[14]:


per_null


# In[15]:


df1.dropna(axis=0,inplace = True)


# In[16]:


sns.heatmap(df1.isnull())


# ## check for the duplicated values 

# In[20]:


dup = df1.duplicated().any()


# In[21]:


dup


# ## Get the overall statistics of dataset

# In[23]:


df1.describe() # include all for all the string and categorical columns 


# ## Display title of the movies having run time more than or equal to 180 minutes 

# In[24]:


df1.columns


# In[25]:


df1.head()


# In[30]:


my_data = df1[df1['Runtime (Minutes)']>=180][['Title','Runtime (Minutes)']]


# In[31]:


sns.barplot(x= 'Runtime (Minutes)',y= 'Title',data = my_data)


# 
# ## IN WHICH YEAR THERE WAS HIGHEST AVERAGE VOTING

# In[32]:


df1.columns


# In[36]:


df1.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# ## In which year there is highest movie revenue

# In[37]:


df1.columns


# In[41]:


df1.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False )


# ## average rating of eacg directors 
# 

# In[42]:


df1.groupby('Director')['Rating'].mean()


# ## top 10 longest movies 

# In[50]:


top_10_len=df1.nlargest(10,'Runtime (Minutes)').sort_values(by='Runtime (Minutes)',ascending=False)[['Title','Runtime (Minutes)']]    .set_index('Title')


# In[54]:


sns.barplot(x='Runtime (Minutes)',y=top_10_len.index,data=top_10_len)


# ## number of movies per year

# In[55]:


df1['Year'].value_counts()


# ## most popular movie titiles as per revenue

# In[56]:


df1.columns


# In[63]:


df1[df1['Revenue (Millions)'].max()==df1['Revenue (Millions)']]['Title']


# In[74]:


top_10_rat=df1.nlargest(10,'Rating').sort_values(by='Rating',ascending=False)[['Title','Director','Rating']].set_index('Title')


# In[75]:


top_10_rat


# In[80]:


sns.barplot(x='Rating',y= top_10_rat.index,data=top_10_rat,hue='Director',dodge=False)
plt.legend(bbox_to_anchor=(1.05,1))
plt.show()


# In[ ]:





# ## top 10 highest revenue titles

# In[85]:


to_rev=df1.nlargest(10,'Revenue (Millions)').sort_values(by='Revenue (Millions)',ascending=False)['Title']


# In[86]:


to_rev


# ## classify movie in three categories

# In[91]:


def rating(rating):
    if rating>=7:
        return "excellent"
    elif rating>=5:
        return "good"
    else:
        return "poor"


# In[92]:


df1['category']= df1['Rating'].apply(rating)


# In[93]:


df1.head()


# ## average rating of movies year wise

# In[94]:


df1.groupby('Year')['Rating'].mean()


# ## does rating affect revenue

# In[96]:


sns.scatterplot(x= 'Rating',y= 'Revenue (Millions)',data=df1)
plt.show()


# ## count the total action movies

# In[98]:


sum(df1['Genre'].str.contains('action',case=False))


# In[ ]:




