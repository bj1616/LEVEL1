#!/usr/bin/env python
# coding: utf-8

# # TASK1: TOP CUISINES

#  ## Determine the top three most common cuisines in the dataset.

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("Dataset.csv")
df.head(5)


# In[3]:


df["Cuisines"].info()


# In[4]:


occurence = df["Cuisines"].value_counts()
occurence


# In[5]:


top_3_cuisines = occurence.head(3)
top_3_cuisines.head(3)


# In[6]:


new_df = pd.DataFrame({'Cuisines':top_3_cuisines.index,'Occurence':top_3_cuisines.values})
new_df.head(3)


# In[7]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.bar(new_df["Cuisines"],new_df["Occurence"],color="green")
plt.xlabel("Cuisines")
plt.ylabel("Occurence")
plt.title("Top 3 Common Cuisines")
plt.show()


# ## Calculate the percentage of restaurants that serve each of the top cuisines.

# In[8]:


res_occ = df["Restaurant Name"].value_counts()


# In[9]:


total_res = len(df)
total_res


# In[10]:


percent_occ = top_3_cuisines/total_res*100


# In[11]:


new_df2 = pd.DataFrame({'Cuisines':top_3_cuisines.index,'Percent_of_res':percent_occ.values})
new_df2


# # Task2: City Analysis

# ## Identify the city with the highest number of restaurants in the dataset

# In[12]:


cities = df["City"].value_counts()
cities


# In[13]:


# Top 5 cities with Highest Number of Restaurants 

cities.head(5)
new_df3 = pd.DataFrame({'City':cities.head(5).index,'No. of restaurant':cities.head(5).values})
new_df3


# In[76]:


plt.figure(figsize = (10,6))
plt.pie(new_df3["No. of restaurant"],labels=new_df3["No. of restaurant"],autopct="%1.1f%%",startangle=140)
plt.legend(new_df3["City"])
plt.title("% of Restaurants in cities")
plt.show()


# ## Calculate the average rating for restaurants in each city

# In[15]:


new_df4 = df[["City","Restaurant Name","Aggregate rating"]]
new_df4


# ## Determine the city with the highest average rating

# In[16]:


new_df4["Aggregate rating"].max()


# In[17]:


new_df4["Aggregate rating"].idxmax()


# In[18]:


new_df4.City[new_df4["Aggregate rating"].idxmax()]


# # Task3: Price Range Distribution

# ## Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants

# In[48]:


count=df["Price range"].value_counts()
count


# In[78]:


plt.figure(figsize=(10,6))
plt.bar(count.index,count.values,color="blue")
plt.xlabel("Price Range")
plt.ylabel("Counts of Restaurants")
plt.title("Distribution of Price Range Among Restaurants")


# ## Calculate the percentage of restaurants in each price range category.

# In[67]:


price_percent = (count/len(df)*100)
price_percent


# In[69]:


new_df5 = pd.DataFrame({'Price range':price_percent.index,'Percent(in %)':price_percent.values})
new_df5


# In[74]:


plt.figure(figsize=(10,6))
plt.pie(new_df5["Percent(in %)"],labels=new_df5["Price range"],autopct="%1.1f%%")
plt.legend(new_df5["Price range"])
plt.title("Percentage of Restaurant in each price Category")
plt.show()


# # Task4: Online Delivery

# ## Determine the percentage of restaurants that offer online delivery

# In[92]:


online = df["Has Online delivery"].value_counts()
online


# In[84]:


online_percent = online/len(df)*100
online_percent


# In[86]:


new_df6 = pd.DataFrame({'Has Online Delivery':online.index,'Percent(in %)':online_percent.values})
new_df6


# In[79]:


df.head(2)


# ## Compare the average ratings of restaurants with and without online delivery

# In[98]:


online_yes = df[df["Has Online delivery"]=="Yes"]


# In[99]:


online_yes["Aggregate rating"].mean()  #average rating of restaurant with online delivery


# In[101]:


online_no = df[df["Has Online delivery"]=="No"]


# In[108]:


online_no["Aggregate rating"].mean()   #average rating of restaurant without online delivery


# In[ ]:




