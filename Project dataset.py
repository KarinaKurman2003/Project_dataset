#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install matplotlib
# !pip install seaborn
# !pip install sweetviz


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st 

st.title("Project dataset")
st.header("Reading Data from computer")
# ### Reading Data from computer

# In[5]:

df = pd.read_csv("/Users/kurmankarina/Desktop/Social_Network_Ads.csv")
df.head(5)

# In[6]:

df.tail(5)



# In[7]:

df.describe()


# In[8]:

st.code("""
df.isna().sum()
""")


# In[9]:


df.info()



# In[10]:


print(f'Shape of df: {df.shape}')



# In[11]:


df.corr()


st.markdown("Our data is structured and does not need data cleanup")
st.header("Add column: 'Age_median'")
# ##### Our data is structured and does not need data cleanup

# ### Add column: 'Age_median'

# In[12]:


df["Age_median"] = df['Age'].median()
df = df.astype({'Age_median': 'int'})



# In[13]:


df.head(5)


st.header("Add column: 'Salary_median'")
# ### Add column: 'Salary_median'

# In[14]:


df["Salary_median"] = df['EstimatedSalary'].median()
df = df.astype({'Salary_median': 'int'})



st.markdown("Check the data again")
# ##### Check the data again

# In[15]:


df.tail(5)



# In[16]:


df.info()



st.header("Data Analysis: part 1")
# ### Data Analysis: part 1
st.markdown("1. How many females/males in data?")
# #### 1. How many females/males in data?

# In[17]:


df['Gender'].value_counts()


st.markdown("2. How many times female/males purchased add object?")
# #### 2. How many times female/males purchased add object?

# In[18]:

print(f"Male: {df[(df['Purchased'] == 1) & (df['Gender'] == 'Male')]['Purchased'].count()}")
print(f"Female: {df[(df['Purchased'] == 1) & (df['Gender'] == 'Female')]['Purchased'].count()}")


st.markdown("3. Median of the salary for male/female?")
# #### 3. Median of the salary for male/female?

# In[19]:


print(f"Male median salary: {df[df['Gender'] == 'Male']['EstimatedSalary'].median()}")
print(f"Female median salary: {df[df['Gender'] == 'Female']['EstimatedSalary'].median()}")


st.header(" Data Analysis: part 2")
# ### Data Analysis: part 2
st.markdown("1. Amount of purchased depents on salary?")
# #### 1. Amount of purchased depents on salary?

# In[20]:


print(f"All purchases: {df[df['Purchased'] == 1]['Purchased'].count()}")
print(f"Amount purchasers with salary less then 30000$: {df[(df['Purchased'] == 1) & (df['EstimatedSalary'] < 30000)]['Purchased'].count()}")
print(f"Amount purchasers with salary from 30000$ to 60000$: {df[(df['Purchased'] == 1) & (df['EstimatedSalary'] <= 30000) & (df['EstimatedSalary'] < 60000)]['Purchased'].count()}")
print(f"Amount purchasers with salary from 60000$ to 90000$: {df[(df['Purchased'] == 1) & (df['EstimatedSalary'] <= 60000) & (df['EstimatedSalary'] < 90000)]['Purchased'].count()}")
print(f"Amount purchasers with salary from 90000$ to 120000$: {df[(df['Purchased'] == 1) & (df['EstimatedSalary'] <= 90000) & (df['EstimatedSalary'] < 120000)]['Purchased'].count()}")
print(f"Amount purchasers with salary from 120000$ to 150000$: {df[(df['Purchased'] == 1) & (df['EstimatedSalary'] <= 120000) & (df['EstimatedSalary'] <= 150000)]['Purchased'].count()}")

st.markdown("From these data, we can conclude that the assumption was correct")
# From these data, we can conclude that the assumption was correct

st.markdown("2. With salary under 20000 people not making a purchases?")
# #### 2. With salary under 20000 people not making a purchases?

# In[21]:


df[(df["EstimatedSalary"] < 20000) & (df['Purchased'] == 1)]['Purchased'].count()


st.markdown("From these data, we can conclude that the assumption was correct")
# From these data, we can conclude that the assumption was correct
st.markdown("3. In an age of 25 till 35 purchases making more often")
# #### 3. In an age of 25 till 35 purchases making more often

# In[22]:


print(f"Amount of purchases made by people under 25 y.o: {df[(df['Age'] < 25) & (df['Purchased'] == 1)]['Purchased'].count()}")
print(f"Amount of purchases made by people older 35 y.o: {df[(df['Age'] > 35) & (df['Purchased'] == 1)]['Purchased'].count()}")
print(f"Amount of purchases made by people from 25 y.o to 35 y.o: {df[(df['Age'] >= 25) & (df['Age'] <= 35) & (df['Purchased'] == 1)]['Purchased'].count()}")


st.markdown("From this data we can conclude that people that over 35 y.o making purchases more often")
# From this data we can conclude that people that over 35 y.o making purchases more often
st.markdown("4. People older then 35 y.o and geting more then 90000 making purchases more often then everybody else")
# #### 4. People older then 35 y.o and geting more then 90000 making purchases more often then everybody else

# In[23]:


print(f"People older 35 and makimg over 90000$: {df[(df['Age'] >= 35) & (df['EstimatedSalary'] >= 90000)]['Purchased'].count()}")
print(f"People younger 35 and makimg less then 90000$: {df[(df['Age'] < 35) & (df['EstimatedSalary'] < 90000)]['Purchased'].count()}")


st.markdown("Assumtion was wrong, situation is opposite ")
# Assumtion was wrong, situation is opposite 
st.markdown("5. Female earn less then male?")
# #### 5. Female earn less then male?

# In[24]:


print(f"Male median salary: {df[df['Gender'] == 'Male']['EstimatedSalary'].median()}")
print(f"Female median salary: {df[df['Gender'] == 'Female']['EstimatedSalary'].median()}")


st.markdown("From the given data assumtion is wrong")
# From the given data assumtion is wrong
st.markdown("6.The average age of a man who makes purchases is greater than the age of women, and because of this, the average salary of this man is greater than that of women")
# #### 6.The average age of a man who makes purchases is greater than the age of women, and because of this, the average salary of this man is greater than that of women

# In[25]:


print(f"Male who purchased median age: {df[(df['Gender'] == 'Male') & (df['Purchased'] == 1)]['Age'].median()}")
print(f"Female who purchased median age: {df[(df['Gender'] == 'Female') & (df['Purchased'] == 1)]['Age'].median()}")
print(f"Male who purchased median salary: {df[(df['Gender'] == 'Male') & (df['Purchased'] == 1)]['EstimatedSalary'].median()}")
print(f"Female who purchased median salary: {df[(df['Gender'] == 'Female') & (df['Purchased'] == 1)]['EstimatedSalary'].median()}")


st.markdown("Thus, the average age of men shopping is less than the age of women, and, moreover, the average salary of women is also higher than that of men")
# Thus, the average age of men shopping is less than the age of women, and, moreover, the average salary of women is also higher than that of men


st.header("Reading Data from computer 2nd dataset")
# ### Reading Data from computer 2nd dataset
st.markdown("Let's add a new dataset in order to test more theories")
# ##### Let's add a new dataset in order to test more theories
st.markdown("Checking the data")
# ##### Checking the data

# In[28]:


df2 = pd.read_csv("/Users/kurmankarina/Desktop/test.csv")
df2.head(5)


# In[29]:


df2.tail(5)



# In[30]:


df2.describe()



# In[31]:



print(f'Shape of df2: {df.shape}')




# In[32]:


df2.isna().sum()



# In[33]:


df2.info()



# In[33]:


df2.corr()


st.header("Data Analysis: part 3")
# ### Data Analysis: part 3
st.markdown("From the previous data analysis, we found out that people with incomes from 120k to 150k are more likely to make purchases, my assumptions are that these are white people and one with higher education")
# ##### From the previous data analysis, we found out that people with incomes from 120k to 150k are more likely to make purchases, my assumptions are that these are white people and one with higher education

# In[35]:

t = df2[(df2['educational-num'] >= 10) & (df2['fnlwgt'] >= 120000) & (df2['fnlwgt'] <= 150000)]['educational-num'].count()
d = df2[(df2['educational-num'] < 10) & (df2['fnlwgt'] >= 120000) & (df2['fnlwgt'] <= 150000)]['educational-num'].count()
y = np.array([t, d])
mylabels = ["HIGHER_EDU", "SCHOOL"]
d = plt.pie(y, labels = mylabels)
plt.legend()
st.pyplot(d)


# In[36]:


t = df2[(df2['race'] == 'White') & (df2['fnlwgt'] >= 120000) & (df2['fnlwgt'] <= 150000)]['educational-num'].count()
d = df2[(df2['race'] != 'White') & (df2['fnlwgt'] >= 120000) & (df2['fnlwgt'] <= 150000)]['educational-num'].count()
y = np.array([t, d])
mylabels = ["WHITE", "NOT"]
q = plt.pie(y, labels = mylabels)
plt.legend()
st.pyplot(q)
# plt.show() 

st.markdown("People who get from 120k to 150k are most often those who got higher education and their race is white ")
# ##### People who get from 120k to 150k are most often those who got higher education and their race is white 
st.header("Data Visualization: part 1")
# ### Data Visualization: part 1
# st.markdown("1. Pairwise dependencies of the features")
# #### 1. Pairwise dependencies of the features

# In[170]:


# z = sns.pairplot(df[['Gender', 'Age', 'EstimatedSalary', 'Purchased', 'Salary_median', 'Age_median']]);

st.markdown("Purchased pie-chart:")

# #### Purchased pie-chart:

# In[35]:


t = df[df['Purchased'] == 1]['Purchased'].count()
d = df[df['Purchased'] == 0]['Purchased'].count()
y = np.array([t, d])
mylabels = ["Purchased", "NOT"]
z = plt.pie(y, labels = mylabels)
plt.legend()
# plt.show() 
st.pyplot(z)

st.markdown("Age of users:")
# #### Age of users:

# In[167]:


e = df.groupby('Gender')['Age'].plot(kind='kde', xlim=[18, 60], legend = True)
st.pyplot(e)

st.markdown("Age and Purchases graf:")
# #### Age and Purchases graf:

# In[25]:


w = df.groupby('Purchased')['Age'].plot(kind='hist', bins=20, legend = True)
st.pyplot(w)

st.markdown("Amount of purchased depents on salary?")
# ####  Amount of purchased depents on salary?

# In[38]:


n = df.groupby('Purchased')['EstimatedSalary'].plot(kind='kde',xlim=[15000, 200000], legend = True)
st.pyplot(n)