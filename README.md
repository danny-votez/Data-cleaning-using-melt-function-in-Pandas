# Data-cleaning-using-melt-function-in-Pandas
In this tutorial, we illustrate data cleaning using melt () function in Pandas
First, there is need to import pandas, then read the dataset for manipulation
<code>
<pre>
# Importing pandas which will allow the data cleaning
import pandas as pd

# Next, it is necessary to read the file, which in this case is a comma separated value (CSV) file

pew = pd.read_csv('d:/dswp/datadanielchen/pew.csv')
</pre>
</code>
- The above code read the dataset from the provided path above

- Then, to visualize our data, we can use the head() function
<code>
<pre>
# Display first 5 rows of the data
pew.head()
</pre>
</code>

To display a different proportion of rows, use "n='desired rows'
For example, pew.head(n=12) gives 12 rows
Image below shows the summary for 12 rows


