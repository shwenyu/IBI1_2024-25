import matplotlib.pyplot as plt  # Import the matplotlib library for plotting

uk_countries = [57.11, 3.13, 1.91, 5.45]  # Define a list of population sizes for UK countries
uk_countries.sort()  # Sort the population sizes in ascending order
label_1 = ["Northern Ireland", "Wales", "Scotland", "Enfland"]  # Define labels for UK countries

Zhe_neighbor = [41.88, 45.28, 61.27, 85.15]  # Define a list of population sizes for Zhejiang neighboring regions
Zhe_neighbor.sort()  # Sort the population sizes in ascending order
label_2 = ["Fujian", "Jiangxi", "Anhui", "Jiangsu"]  # Define labels for Zhejiang neighboring regions

print(uk_countries, Zhe_neighbor)  # Print the sorted population sizes for both regions

plt.pie(uk_countries, labels=label_1, autopct='%1.1f%%')  # Create a pie chart for UK population sizes with labels and percentages
plt.title("Population size of UK")  # Set the title for the UK pie chart

plt.show()  # Display the UK pie chart

plt.pie(Zhe_neighbor, labels=label_2, autopct='%1.1f%%')  # Create a pie chart for Zhejiang neighboring population sizes with labels and percentages
plt.title("Population size of Zhejiang Neighboring")  # Set the title for the Zhejiang neighboring pie chart

plt.show()  # Display the Zhejiang neighboring pie chart