# moths_in_house = True
moths_in_house = False
if(moths_in_house):
    print("Get the moths!")
else:
    print("No threats detected.")
############# Q2 #####################
moths_in_house = True
mitch_is_home = True
if(moths_in_house and mitch_is_home):
    print("Hoooman! Help me get the moths!")
# moths_in_house = False
# mitch_is_home = False
elif(not moths_in_house and not mitch_is_home):
 print("No threats detected.")
# moths_in_house = True
# mitch_is_home = False
elif(moths_in_house and not mitch_is_home):
    print("Meooooooooooooow! Hissssss!")
# moths_in_house = False
# mitch_is_home = True
elif(not moths_in_house and mitch_is_home):
    print("Climb on Mitch.")
############ Q3 ####################
light_colour = "Red"
car_detected = True
if ((light_colour == "Red")and car_detected):
    print("flash !!!!!!!")
else:
    print("Do Nothing")
############ Q4 ####################
height = int(input("Enter your height "))
if(height >= 120):
    print("Hop on!")
else:
    print("Sorry, not today :(")