#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ### Q.1: Writer pandas series code to get following output without using dictionary: 

# In[2]:


df= pd.Series(data = ['a','x','c','2','e'],index = ['1','4','9','6','7'])
df


# In[3]:


df


# ### Q.2: Writer pandas series code to get following output using dictionary:
# 

# In[4]:


# Question no 2

data = {
    'Bilal':42,
    'Ayesha':38,
    'Hadia':39
}
pd.Series(data)


# ### .3: Write pandas dataframe code to get following output using python dictionary
# 

# In[5]:


# Questionn no 3

dic ={
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}

df =pd.DataFrame(dic)
df


# ## Q.4: In extension to above question, you are required to replace index by ['a','b','c','d','e','f']
# 

# In[6]:


df =pd.DataFrame(dic,index=['a','b','c','d','e','f'])
df


# ### Q.5: In extension to above Q.3, calculate mean, miximum and minimum for label “temperature”

# In[7]:


# mean of the temperature
df['temperature'].mean()


# In[8]:


# maximum of temperature
df['temperature'].max()


# In[9]:


# minimum of temperature 
df['temperature'].min()


# ### Q.6: Import CSV ‘people.csv’ in the given folder. Keep in mind the following instructions: You’re required to import only specific columns ["First Name", "Sex", "Email", “Phone”, “Job Title”] Set the following columns ["Sex", "Job Title"] as index columns Skip following rows [1,5] Export the CSV as “NewPeople.csv” 

# In[10]:


df =pd.read_csv('people.csv',usecols=['First Name','Sex','Email','Phone','Job Title'])
df


# In[11]:


df=pd.read_csv('people.csv',usecols=['First Name','Sex','Email','Phone','Job Title'],index_col=['Sex','Job Title'])
df


# In[ ]:





# In[12]:


df=pd.read_csv('people.csv',usecols=['First Name','Sex','Email','Phone','Job Title'],index_col=['Sex','Job Title'],skiprows=[1,5])

df


# **-> Export the CSV as “NewPeople.csv”**

# In[13]:


df.to_csv('NewPeople')


# In[14]:


# """Q.7: Import excel sheet ‘SampleWork.xlsx’ in the given folder. Keep in mind the following instructions:
# Import sheet 1
# Import only first and last column from sheet 1
# Skip row 2 while importing the sheet
# Set row 2 as header
# export as new sheet.d"""


# In[15]:


pd.read_excel('SampleWork.xlsx',sheet_name='Sheet1')


# In[16]:


pd.read_excel('SampleWork.xlsx',sheet_name='Sheet1',usecols=[0,3])


# In[17]:


pd.read_excel('SampleWork.xlsx',sheet_name='Sheet1',usecols=[0,3],skiprows=[1])


# In[18]:


df=pd.read_excel('SampleWork.xlsx',sheet_name='Sheet1',usecols=[0,3],header=[2])
df


# pd.to_excel('SampleWork.xlsx'

# In[19]:


fname = 'SampleWork.xlsx'
 
with pd.ExcelWriter(fname) as writer:
    df.to_excel(writer, sheet_name='sheet4', index=False)


# ### Question no 8: Create the following dataframe as AICP_DF then implement different operations as described below select 'Name', 'Qualification' coloumns and save to df1 add a new column to AICP_DF “Height” with the following values: [5.1, 6.2, 5.1, 5.2,5.1]set column “Name” as the index column. retrieve row with index “Hifza” retrieve row with index 3 drop row with index “Bilal

# In[22]:


data = {
    'Name':['Sonia','Bilal','Hifza','Kabir','jazim'],
    'Age':[27,24,22,32,23],
    'Address':['Lahore','Karachi','Sialkot','Peshawar','Ihr'],
    'Qualification':['Msc','MA','MCA','Phd','bsc']
}
AICP_DF=pd.DataFrame(data)


# In[23]:


AICP_DF


# In[24]:


# select 'Name','Qualification'columns and save to df1

df1 = AICP_DF[['Name','Qualification']]
df1


# In[25]:


# add a new column to AICP_DF “Height” with the following 
# values: [5.1, 6.2, 5.1, 5.2,5.1]

AICP_DF['Height']=[5.1,6.2,5.1,5.2,5.1]
AICP_DF


# In[27]:


# h the following values: [5.1, 6.2, 5.1, 5.2,5.1]
# set column “Name” as the index column

AICP_DF=AICP_DF.set_index('Name')
AICP_DF


# In[28]:


# retrieve row with index “Hifza”
AICP_DF.loc['Hifza']


# In[29]:



#retrieve row with index 3

AICP_DF.iloc[3]


# In[30]:


# drop row with index “Bilal”
AICP_DF.drop('Bilal')


# In[ ]:




