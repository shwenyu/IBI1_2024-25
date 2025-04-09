import matplotlib.pyplot as plt  # Import the matplotlib library for plotting
import pandas as pd  # Import the pandas library for data manipulation

Table2 = pd.read_excel("Table2.xlsx")  # Read the Excel file "Table2.xlsx" into a DataFrame
uk_countries = list(Table2[Table2['Nation'] == "UK"]["Population"])  # Filter rows where 'Nation' is "UK" and extract the 'Population' column as a list
uk_countries.sort()  # Sort the list of populations in ascending order
label_1 = ["Northern Ireland", "Wales", "Scotland", "Enfland"]  # Define labels for UK countries
print(uk_countries)  # Print the sorted list of UK populations

zhejiang_neighbor = list(Table2[(Table2['Country/Province'] == "Fujian")  # Filter rows where 'Country/Province' is one of the specified provinces
                                | (Table2['Country/Province'] == "Jiangxi")
                                | (Table2['Country/Province'] == "Anhui")
                                | (Table2['Country/Province'] == "Jiangsu")]["Population"])  # Extract the 'Population' column as a list
zhejiang_neighbor.sort()  # Sort the list of populations in ascending order
label_2 = ["Fujian", "Jiangxi", "Anhui", "Jiangsu"]  # Define labels for neighboring provinces of Zhejiang
print(zhejiang_neighbor)  # Print the sorted list of populations for Zhejiang's neighbors

# print(Table2)  # Uncomment to print the entire DataFrame (currently commented out)

use = "Python"  # Define the programming language to analyze
lan = {"Javascript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5}  # Define a dictionary with programming languages and their usage percentages
sums = sum(lan.values())  # Calculate the sum of all usage percentages
usenum = lan[use]  # Get the usage percentage of the selected language
print("The percentage of this language is:", usenum / sums * 100, "%")  # Print the percentage of the selected language relative to the total

for i in lan.keys():  # Iterate through each key in the dictionary
    print("the key is:", i, "the value is:", lan[i])  # Print the key (language) and its value (usage percentage)

x = list(lan.keys())  # Extract the keys (languages) as a list
y = list(lan.values())  # Extract the values (usage percentages) as a list
fig, axs = plt.subplots(2, 2, figsize=(10, 5))  # Create a 2x2 grid of subplots with a specified figure size

axs[0, 0].pie(uk_countries, labels=label_1, autopct='%1.1f%%')  # Create a pie chart for UK populations with labels and percentages
axs[0, 0].set_title('Pie Chart: UK')  # Set the title for the first subplot

axs[0, 1].pie(zhejiang_neighbor, labels=label_2, autopct='%1.1f%%')  # Create a pie chart for Zhejiang's neighboring provinces
axs[0, 1].set_title('Pie Chart: Zhejiang Neighbor')  # Set the title for the second subplot

axs[1, 0].bar(x, y, color="#22E5E5")  # Create a bar chart for programming language usage percentages
plt.tight_layout()  # Adjust the layout to prevent overlapping elements
plt.show()  # Display the plots
