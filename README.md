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

![image](https://user-images.githubusercontent.com/77758884/131687204-4ea7fd4d-7d4c-40b7-aa6b-ad98b122d02f.png)


To display a different proportion of rows, use "n='desired rows'
For example, pew.head(n=12) gives 12 rows
Image below shows the summary for 12 rows
![image](https://user-images.githubusercontent.com/77758884/131686585-913631ef-fa17-4088-8560-a285dbf310ba.png)

Next, based on the printed dataset, it seems "religion" column is well placed, while income is spread across different columns
We can use the "melt()" function to keep the "religion" column, and transform the other columns into one or two
In this exercise, the aim is to keep religion as it is;

<code>
<pre>
pew_long = pd.melt(pew, id_vars='religion')
</pre>
</code>

The image below shows the output, with only three columns

![image](https://user-images.githubusercontent.com/77758884/131687897-5d4cdcba-c67b-4b26-87dd-74afba3bcaaf.png)
