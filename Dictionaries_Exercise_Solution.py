# groceries = {
# "Baby Spinach": 2.78,
# "Hot Chocolate": 3.70,
# "Crackers": 2.10,
# "Bacon": 9.00,
# "Carrots": 0.56,
# "Oranges": 3.08
# }
# units = []
# index = 0
# total = 0
# for item in groceries:
#     units.append(int(input(" how many units of item {} did you buy? ".format(item))))
# print("")
# print("====Izzy's Food Emporium====")
# for item, values in groceries.items():
#     print("{:<20} ${:.2f}".format(item,values * units[index]))
#     total += values * units[index]
#     index += 1
# print("============================")
# print("{:<20} ${:.2f}".format('',total))
########################## Q2 ###################
names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]
# Creating an empty dictionary 
myDict = {} 
for items in names:
    x = myDict.get(items,0) + 1
    myDict[items] = x
# print(myDict)

########################## Q3 ###################
import csv
color_list = []
final_colour_list = []
with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        color_list.append(line)
header = color_list[0]
del color_list[0]  
for line in color_list:
    color_dict ={}
    for i in range(len(header)):
        color_dict[header[i]]= line[i]
    final_colour_list.append(color_dict)
print(final_colour_list)
