#BEGIN
    #IMPORT matplotlib.pyplot as plt
    #IMPORT pandas as pd

    #READ the Excel file "Table2.xlsx" into a DataFrame named Table2

    #EXTRACT the population data for UK countries from Table2 and STORE it in a list named uk_countries
    #SORT the list uk_countries
    #DEFINE a list of labels for UK countries as label_1
    #PRINT the list uk_countries

    #EXTRACT the population data for Zhejiang's neighboring provinces from Table2 and STORE it in a list named zhejiang_neighbor
    #SORT the list zhejiang_neighbor
    #DEFINE a list of labels for Zhejiang's neighboring provinces as label_2
    #PRINT the list zhejiang_neighbor

    #PROMPT user to input the programming language they use and STORE it in variable use
    #DEFINE a dictionary lan with programming languages as keys and their usage percentages as values
    #CALCULATE the sum of all values in the dictionary lan and STORE it in variable sums
    #GET the usage percentage of the language specified by the user from the dictionary lan and STORE it in variable usenum
    #PRINT the percentage of the specified language

    #FOR each key in the dictionary lan
        #PRINT the key and its corresponding value
    #END FOR

    #CONVERT the keys of the dictionary lan to a list and STORE it in variable x
    #CONVERT the values of the dictionary lan to a list and STORE it in variable y

    #CREATE a 2x2 subplot figure with size 10x5
    #PLOT a pie chart of uk_countries with labels label_1 in the first subplot
    #SET the title of the first subplot to 'Pie Chart: UK'
    #PLOT a pie chart of zhejiang_neighbor with labels label_2 in the second subplot
    #SET the title of the second subplot to 'Pie Chart: Zhejiang Neighbor'
    #PLOT a bar chart of x and y with color "#22E5E5" in the third subplot

    #ADJUST the layout of the subplots
    #DISPLAY the figure
#END
import matplotlib.pyplot as plt
import pandas as pd
Table2 = pd.read_excel("Table2.xlsx")
uk_countries = list(Table2[Table2['Nation'] == "UK"]["Population"])
uk_countries.sort()
label_1 = ["Northern Ireland","Wales","Scotland","Enfland"]
print(uk_countries)
zhejiang_neighbor = list(Table2[(Table2['Country/Province'] == "Fujian") 
                                | (Table2['Country/Province'] == "Jiangxi")
                                | (Table2['Country/Province'] == "Anhui")
                                | (Table2['Country/Province'] =="Jiangsu") ]["Population"])
zhejiang_neighbor.sort()
label_2 = ["Fujian","Jiangxi","Anhui","Jiangsu"]
print(zhejiang_neighbor)
#print(Table2)
use = "Python" #This is the variable that can be modified to show the certain percentage of this language
lan = {"Javascript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}
sums = sum(lan.values())
usenum = lan[use]
print("The percentage of this language is:", usenum/sums*100,"%")
for i in lan.keys():
    print("the key is:", i, "the value is:", lan[i])
x = list(lan.keys())
y = list(lan.values())
fig, axs = plt.subplots(2,2,figsize=(10,5))
axs[0,0].pie(uk_countries, labels=label_1, autopct='%1.1f%%')
axs[0,0].set_title('Pie Chart: UK')
axs[0,1].pie(zhejiang_neighbor, labels= label_2, autopct='%1.1f%%')
axs[0,1].set_title('Pie Chart: Zhejiang Neighbor')
axs[1,0].bar(x,y,color = "#22E5E5")
plt.tight_layout()
plt.show()
