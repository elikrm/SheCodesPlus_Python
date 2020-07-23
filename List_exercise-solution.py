########Q1###########
foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]
# The first item in the list.
print(foods[0])
# 2. The third item in the list.
print(foods[2])
# 3. The last item in the list.
print(foods[-1])
# 4. The first three items in the list.
print(foods[0:3])
# 5. The last three items in the list.
print(foods[-3:])
# 6. The last item in the sublist.
print(foods[6][-1])

###########Q2################
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]
for item in mailing_list:
    print("{} : {}".format(item[0],item[1]))
nameList = []
for i in range(3):
    enterName =input("enter a name: ")
    nameList.append(enterName)
print(nameList)

###########Q3#####################
yourlist = input("Enter a sentence: ")
wordlist = yourlist.split()
print(len(wordlist),wordlist)
letterlist= list(yourlist)
print(len(letterlist),letterlist)
