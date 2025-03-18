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
print(Table2)
use = input("Which language you use:")
lan = {"Javascript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}
sums = sum(lan.values())
usenum = lan[use]
print("The percentage of this language is:", usenum/sums*100,"%")
for i in lan.keys():
    print("the key is:", i, "the value is:", lan[i])
x = list(lan.keys())
y = list(lan.values())
plt.pie(uk_countries, labels=label_1)
plt.pie(zhejiang_neighbor, labels= label_2)
#plt.bar(x,y,color = "#22E5E5")
plt.show()
