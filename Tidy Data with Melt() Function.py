#!/usr/bin/env python
# coding: utf-8

# In[101]:


# Importing pandas which will allow the data cleaning
import pandas as pd

# Next, it is necessary to read the file, which in this case is a comma separated value (CSV) file

pew = pd.read_csv('d:/dswp/datadanielchen/pew.csv')

# Display first 5 rows of the data
pew.head()


# In[103]:


# To display a different proportion of rows, use "n='desired rows'
# For example
pew.head(n=12)               # Gives 12 rows


# In[104]:


# We do not want to change the religion column
pew_long = pd.melt(pew, id_vars='religion')


# In[105]:


pew_long.head(n=12)


# In[106]:


pew_long.head()


# In[107]:


# We can now change and specify the default variable and value names
# This is done by using the var_name and value_name functions
# For example changing the variable above to "Income"
# And changing the value to "Count"

pew_long = pd.melt(pew, id_vars='religion', var_name='Income', value_name='Count')


# In[108]:


pew_long.head(n=10)


# In[109]:


pew_long


# In[110]:


# We can use the .shape method to see the differences in the dataframe upon applying melt() method
pew.shape


# In[113]:


# The above shows the original data has 18 rows and 11 columns

# We can then check the shape for the adjusted pew dataset
pew_long.shape


# In[112]:


# The above shows the new data frame has 180 rows and 3 columns
# This is as shown below
pew_long


# In[114]:


pew_long.columns


# In[115]:


pew_long.head(n=10)


# In[116]:


# We can print the religion column at index 2
pew_long.loc[2]


# In[117]:


# We can also visualize rows at 2 and 6 and 18 as shown below
pew_long.loc[[2,6, 12]]


# In[118]:


# If we need to get all rows in which the Religion is "Agnostic"
# And print or filter based on the religion, Income and Count 
subsetAgnostic = pew_long.loc[pew_long['religion'] == 'Agnostic', ['religion', 'Income', 'Count']]
subsetAgnostic


# In[124]:


# If we need to get all rows in which the Religio is "Agnostic"
# And print or filter based on the religion, Income and Count 
subsetAgnostic = pew_long.loc[(pew_long['religion'] == 'Agnostic') & (pew_long['Income'] == '>150k'),
                              ['religion', 'Income', 'Count']]
subsetAgnostic


# In[125]:


# If we need to get all rows in which the Religio is "Agnostic"
# And print or filter based on the religion, Income and Count 
subsetMuslim = pew_long.loc[(pew_long['religion'] == 'Muslim') & (pew_long['Income'] == '>150k'),
                              ['religion', 'Income', 'Count']]
subsetMuslim

