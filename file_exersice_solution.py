names = []
with open("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)
# print(names)
with open("names_output.txt", "w") as txt_file:
    # for name in names:
    #     txt_file.write(name + '\n')
    print("#########Printing Q1 Output######")
    for count, item in enumerate(names):
        print(count, item)
        txt_file.write(str(count+1) + ". " + item + '\n')

############Q2
import csv
color_list = []
with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        color_list.append(line)
# Writing to CSV file
with open('colour_20_results_output.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for item in color_list:
        # use .strip() on a string to remove whitespace
        csv_writer.writerow(["{:<20} {:<20} {}".format(item[1].strip(), item[2].strip(),item[4].strip())])

####for colours_213.csv
color_list = []
with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        color_list.append(line)
# print(color_list)
       
# Writing to CSV file
with open('colour_213_results_output.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for item in color_list:
        csv_writer.writerow(["{:<20} {:<20} {}".format(item[1].strip(), item[2].strip(),item[4].strip())])

############Q3
color_list = []
red_counter =0
green_counter = 0
blue_counter =0 
English_Name =[]
with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        color_list.append(line)
for item in color_list:
    English_Name.append(item[4])
    # print(English_Name)
for item in English_Name:
    if 'red' in item.lower():
        red_counter +=1
        # print(item)
    if 'green' in item.lower():
        green_counter += 1
    if 'blue' in item.lower():
        blue_counter += 1
print("#########Printing Q3 Output######")
print("Red:" + str(red_counter))
print("Green: " + str(green_counter))
print("Blue: " +str(blue_counter))
        
