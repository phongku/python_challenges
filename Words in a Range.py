# Type your code here. 
file_name = input()
list_start = input()
list_end = input()

file = open(file_name, 'r')

fileList = file.readlines()

for item in fileList:
    item = item.replace('\n','')
    if(item >= list_start and item <= list_end):
        print(item,'- in range')
    else:
        print(item,'- not in range')
