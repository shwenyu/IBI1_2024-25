import matplotlib.pyplot as plt  # Import the matplotlib library for plotting
table = {"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}  # Define a dictionary with programming languages and their popularity percentages
lan = "Python"  # Set the variable 'lan' to the language of interest
summ = sum(table.values())  # Calculate the sum of all popularity percentages
percent = table[lan]/summ  # Calculate the percentage contribution of the selected language
x = list(table.keys())  # Extract the keys (language names) from the dictionary as a list
y = list(table.values())  # Extract the values (popularity percentages) from the dictionary as a list
plt.bar(x,y)  # Create a bar chart with languages on the x-axis and their popularity on the y-axis
plt.title("Language Popularity")  # Set the title of the bar chart
plt.show()  # Display the bar chart