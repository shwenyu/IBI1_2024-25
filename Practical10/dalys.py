import os #Import the os library for operating system functions
import pandas as pd #Import the pandas library for data manipulation
import numpy as np #Import the numpy library for numerical operations
import matplotlib.pyplot as plt #Import the matplotlib library for plotting
os.chdir('Practical10') #Set the current working directory to 'Practical10'
#os.getcwd() #Check the current working directory
#os.listdir() #List the files in the current directory
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv') #Read the CSV file 'dalys-rate-from-all-causes.csv' into a DataFrame
#dalys_data.info() # check the data types and non-null counts
#print(dalys_data.head()) # check the first 5 rows
print(dalys_data.describe()) # summary statistics
#print(dalys_data.iloc[0:2,0]) #check the specific value
print(dalys_data.iloc[0:10,2]) # print the first 10 rows of the 3rd column(Year), and the 10th year of DALYs in Afghanistan is 1999
print(dalys_data.iloc[0:5:2,:]) # print every 2nd row of the first 5 rows
#print(dalys_data.iloc[[0,2],[0,2]])
my_columns = [True, True, False,False]
# Define a boolean list to filter specific columns.

print(dalys_data.iloc[0:3,my_columns],'\n') #only show the 1st, 2nd, and 4th columns with the first 3 rows
print(dalys_data.loc[0:5,'Entity'],'\n') #loc is based on the index name while iloc is based on the index number
select_1990 = []
# Initialize an empty list to store boolean values for filtering rows.

for i in range(len(dalys_data)):
    if dalys_data['Year'][i] == 1990:
        select_1990.append(True)
    else:
        select_1990.append(False)
# Iterate through the DataFrame and append True to the list if the year is 1990, otherwise append False.

print(dalys_data.loc[select_1990,'DALYs']) #use Boolean indexing to select the rows where the year is 1990
print(dalys_data.loc[dalys_data.Year == 1990,'DALYs']) # this is a more efficient way to do the same thing
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]] # select the DALYs and Year columns for the UK
france = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]] # select the DALYs and Year columns for France
print("The DALys of France is",france.DALYs.mean()) # mean of DALYs in France
print("The DALys of UK is",uk.DALYs.mean()) # mean of DALYs in the UK
plt.plot(uk.Year, uk.DALYs, 'go-') # "g/r/b" is the color of the line, "o/+/*" is the marker, "- or empty" is the line style
plt.xticks(uk.Year,rotation=90) # rotate the x-axis labels for better readability
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in the UK')
plt.show()
#Following is the manipulation of DALYs of the world along time
year_group = dalys_data.groupby('Year', as_index=False) # as_index=False means that the groupby object will not use the group labels as the index, and groupby will return a DataFrame with the same index as the original DataFrame
year_group_mean = year_group.DALYs.mean() # calculate the mean of DALYs for each year
#print(year_group_mean)
plt.plot(year_group_mean.Year, year_group_mean.DALYs, 'bo-')
plt.xticks(rotation=90) # rotate the x-axis labels for better readability
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs in the world')
plt.show()
