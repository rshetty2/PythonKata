import pandas as pd
fl = pd.read_csv('../bhp.csv')

df = pd.DataFrame(fl)
print(df.head(10))
df.isnull().sum()

'''
1. Load the CSV file into a pandas DataFrame.
2. Display the first 10 rows of the dataset.
3. Display the shape (number of rows and columns) of the dataset.
4. Show the summary information of the dataset (data types, non-null counts).
5. Select only the 'location' column from the DataFrame.
6. Select the 'location', 'size', and 'total_sqft' columns.
7. Select the first 5 rows of the DataFrame.
8. Check for missing values in each column of the dataset.
9. Drop rows with missing values.
10. Replace missing values in the 'size' column with the string 'Unknown'.
11. Fill missing values in numerical columns with the mean of the respective column.
12. Sort the DataFrame based on the 'price' column in descending order.
13. Create a new column called 'price_per_sqft' by dividing 'price' by 'total_sqft'.
14. Replace all values in the 'size' column where the value is '1 BHK' with '1 Bedroom'.
15. Drop the 'availability' column from the dataset.
16. Select rows where the 'price' is greater than 1 crore (10 million).
17. Select rows where the 'location' is 'Whitefield'.
18. Select rows where the 'size' is '2 BHK' and 'price' is less than 50 lakhs (5 million).
19. Select rows where the 'location' contains the word 'Indira'.
20. Select rows where the 'total_sqft' is missing.
21. Group the data by 'location' and calculate the average 'price' for each location.
22. Find the total number of houses available in each 'location'.
23. Group by 'size' and find the maximum 'price' for each size.
24. Find the total 'price' for all houses in the 'Whitefield' location.
25. Set 'location' as the index of the DataFrame.
26. Reset the index back to the default integer index.
27. Select the rows where the index label is 'HSR Layout'.
28. Use the `.iloc` method to select the first 3 rows and first 4 columns.
29. Use the `.loc` method to select all rows where the 'location' is 'Yelahanka' and display 'price' and 'size'.
30. Find the unique values in the 'size' column.
31. Count the occurrences of each unique value in the 'location' column.
32. Find the number of unique values in the 'area_type' column.
33. Select rows where 'price_per_sqft' is above the average 'price_per_sqft'.
34. Select rows where the 'location' starts with 'B' and 'size' is '3 BHK'.
35. Select rows where 'price' is between 20 lakhs and 80 lakhs (2 million and 8 million).
36. Select rows where 'total_sqft' is greater than 2000 but 'price_per_sqft' is less than 5000.
37. Drop rows where any column has missing data.
38. Replace missing values in the 'bath' column with the median value of the column.
39. Perform one-hot encoding on the 'area_type' column.
40. Use one-hot encoding on the 'location' column and keep only the top 5 most frequent locations.
41. Find the mean, median, and standard deviation of the 'price' column.
42. Calculate the correlation matrix for all numeric columns in the dataset.
43. Find the count of rows where 'total_sqft' is greater than 1500 and 'bath' is less than 3.
'''