
# ### Q.1:Import libraries (Numpy, pandas, matplotlib, plotly and seaborn) and then read csv file.



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# #### Q.2: Check statistical facts by checking all columns. Then calculate the maximum value of the following attributes ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 'Iron (% Daily Value)']

df =pd.read_csv('menu.csv',usecols=['Calories', 'Total Fat', 'Carbohydrates',
                                    'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin A (% Daily Value)',
                                    'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 'Iron (% Daily Value)'])

print(df.head(5))


# ### Q.3: Check to see if infact there is any correlation between Calories and other
# independent variables by plotting a correlation matrix next.


sns.heatmap(df.corr())
ax = plt.gca()
plt.grid()
ax.xaxis.tick_top()
ax.tick_params(axis='x', rotation=40)




# ### Q.4: Draw boxplot for Calories vs Category to spot outliers and max calories category


df1 = pd.read_csv('menu.csv')



sns.boxplot(y='Category', x='Calories', data=df1,hue='Category')


# ##### Q.5: Figure out which exact item contains a high quantity for ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 'Calcium (% Daily Value)', 'Iron (% Daily Value)'. Display summary link this:

# In[41]:


lis = []
for i in df.columns:
    lis.append(i)



print(lis)




# i want to make a list after combining all the requied values i want to store in this list
new_lis=[]
for value in lis:
    new_value = f'{value} : ' + df1[df1[f'{value}']==df1[f'{value}'].max()]['Item'].values[0] + "   -   " + str(df1[f'{value}'].max())
    new_lis.append(new_value)

# now i want to show the summary 
for summary in new_lis:
    print(summary)


# ### Q.6: Draw Stripplot for each category against the following attributes ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)','Calcium (% Daily Value)', 'Iron(% Daily Value)'.
# ### Here is one sample, you have to do it for all above mentioned attributes in list.




# Category and Calories

sns.stripplot(data = df1,x='Category',y= 'Calories')
plt.xticks(rotation=70)
plt.show()


# In[45]:


# Category and Total Fat

sns.stripplot(data = df1,x='Category',y= 'Total Fat')
plt.xticks(rotation=70)
plt.show()


# In[46]:


# Category and Carbohydrates

sns.stripplot(data = df1,x='Category',y= 'Carbohydrates')
plt.xticks(rotation=70)
plt.show()




# Category and Dietary Fiber

sns.stripplot(data = df1,x='Category',y= 'Dietary Fiber')
plt.xticks(rotation=70)
plt.show()


# In[48]:


# Category and Sugars

sns.stripplot(data = df1,x='Category',y= 'Sugars')
plt.xticks(rotation=70)
plt.show()

# Category and Protein

sns.stripplot(data = df1,x='Category',y= 'Protein')
plt.xticks(rotation=70)
plt.show()



# Category and Vitamin A (% Daily Value)'
sns.stripplot(data = df1,x='Category',y= 'Vitamin A (% Daily Value)')
plt.xticks(rotation=70)
plt.show()



# Category and Vitamin C (% Daily Value)

sns.stripplot(data = df1,x='Category',y= 'Vitamin C (% Daily Value)')
plt.xticks(rotation=70)
plt.show()



# Category and Calcium (% Daily Value)

sns.stripplot(data = df1,x='Category',y= 'Calcium (% Daily Value)')
plt.xticks(rotation=70)
plt.show()



# Category and 'Iron(% Daily Value)'

sns.stripplot(data = df1,x='Category',y= 'Iron (% Daily Value)')
plt.xticks(rotation=70)
plt.show()


# ### Q.7: Draw a horizontal bar graph for items in each category against the calories. Here is one sample for all items in Beef & Pork, you have to do it for items in each category. Also, write your observation.
# 


# last question 

df1.head(3)


# In[55]:


sns.barplot(data=df1,x='Calories',y='Category')




# MY OBSERVATION

# this bar graph show error bar on the bar graph









