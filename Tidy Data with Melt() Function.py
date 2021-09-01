#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Importing pandas which will allow the data cleaning
import pandas as pd

# Next, it is necessary to read the file, which in this case is a comma separated value (CSV) file

pew = pd.read_csv('d:/dswp/datadanielchen/pew.csv')

# Display first 5 rows of the data
pew.head()


# In[78]:


# To display a different proportion of rows, use "n='desired rows'
# For example
pew.head(n=12)               # Gives 15 rows


# In[75]:


# We do not want to change the religion column
pew_long = pd.melt(pew, id_vars='religion')


# In[5]:


pew_long


# In[6]:


pew_long.head()


# In[7]:


# We can now change and specify the default variable and value names
# This is done by using the var_name and value_name functions
# For example    changing the variable above tp income
# And changing the value 
pew_long = pd.melt(pew, id_vars='religion', var_name='Income', value_name='Count')


# In[8]:


pew_long.head(n=10)


# In[37]:


# We can print the religion column at index 2
pew_long.loc[2]


# In[47]:


# We can also visualize rows at 2 and 6 and 18 as shown below
pew_long.loc[[2,6, 12]]


# In[51]:


# If we need to get all rows in which the Religio is "Agnostic"
# And print or filter based on the religion, Income and Count 
subsetAgnostic = pew_long.loc[pew_long['religion'] == 'Agnostic', ['religion', 'Income', 'Count']]
subsetAgnostic


# In[71]:


# If we need to get all rows in which the Religio is "Agnostic"
# And print or filter based on the religion, Income and Count 
subsetAgnostic = pew_long.loc[(pew_long['religion'] == 'Muslim') & (pew_long['Income'] == '>$10k'), ['religion', 'Income', 'Count']]
subsetAgnostic

