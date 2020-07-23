# #Q1) Continuously ask the user to enter a number until they provide a blank input. 
# # Output the sum of all the numbers.

# # isnumeric() Returns True if all characters in the string are numeric
# # isspace()	Returns True if all characters in the string are whitespaces
# yournumber = input("Enter a number: ")
# totalnumber = 0
# while((len(yournumber)!=0) and (yournumber.isnumeric()) and not(yournumber.isspace())):
# # while(len(yournumber)!=0):
#     # print(yournumber.isnumeric())
#     # print(not yournumber.isspace())
#     totalnumber = totalnumber + int(yournumber)
#     yournumber = input("Enter a number: ")
# print(totalnumber)
# #Q2) Use a for loop to format and print the following list:
# mailing_list = [
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Biscuit", "biscuit@whippies.park"],
# ["Rory", "rory@whippies.park"],
# ]
# for item in mailing_list:
#     print("{} : {}".format(item[0],item[1]))
# nameList = []

# # Q3) Use a while loop to ask the user for three names and append them to a list, 
# # then use a for loop to print the list.
# counter = 3
# nameList = []
# while(counter>0):
#     enterName =input("enter a name: ")
#     nameList.append(enterName)
#     counter -= 1
# print(nameList)

#Q4) Ask the user how many units of each item they bought, 
# then output the corresponding receipt.
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]
units = []
index = 0
total = 0
for item in groceries:
    units.append(int(input(" how many units of item {} did you buy? ".format(item[0]))))
print("")
print("====Izzy's Food Emporium====")
for item in groceries:
    print("{:<20} ${:.2f}".format(item[0],item[1] * units[index]))
    total += item[1] * units[index]
    index += 1
print("============================")
print("{:<20} ${:.2f}".format('',total))