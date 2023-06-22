import csv

# Type your code here. 
file_name = input()
file = open(file_name)
data = csv.reader(file, delimiter = ',')

master_list = []
for row in data:
    for word in row:
        master_list.append(word.strip())

for i in range(len(master_list)):
    if master_list[i] not in master_list[:i]:
        count = 0
        for w in master_list:
            if master_list[i] == w:
                count += 1
        print(str(master_list[i]) + ' - ' + str(count))
file.close()
