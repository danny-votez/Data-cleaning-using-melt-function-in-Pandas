# Data-cleaning-using-melt-function-in-Pandas
In this tutorial, we illustrate data cleaning using melt () function in Pandas
First, there is need to import pandas, then read the dataset for manipulation

# Importing Pandas and Reading the File
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

# Using melt() method in Tidying/Cleaning the Data 

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


Next, We can use the .shape method to see the differences in the dataframe upon applying melt() method

![image](https://user-images.githubusercontent.com/77758884/131688726-ebdc6d20-5cf8-49a9-aac7-8a16e46f8d2a.png)

As seen above, the original dataframe had 18 rows and 11 columns, while the adjusted/second dataframe has 180 rows and 3 columns.


The visualization below shows this is true
![image](https://user-images.githubusercontent.com/77758884/131688572-19495f92-f294-481f-a3a9-bdc33f31fa65.png)


# Some Manipulations

We can print the religion column at index 2 using the .loc (location) method. 

"loc" calls for pulling out rows based on how they are labelled

![image](https://user-images.githubusercontent.com/77758884/131689221-7b74f28f-feae-4b30-b8b9-0ce03be7e7c6.png)

The summary shows that at index 2, religion is Buddhist, with Income of <$10k and Count 27

We can also get data for three elements, i.e., 2, 6, and 12, as shown below;
![image](https://user-images.githubusercontent.com/77758884/131689633-0311c114-288e-4e24-968a-0ed48dad4d15.png)

Next, we can also get specific items from the data. For example, in the illustration below, the goal is to get all rows in which the Religion is "Agnostic".
 And then, there is pulling and printing/filter the rows based on the religion, Income and Count columns
 
 ![image](https://user-images.githubusercontent.com/77758884/131689988-ee8e0ab8-2071-4404-b3a8-274bd70b3e5f.png)

 
 

