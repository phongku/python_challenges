import os

filename = input()

with open(filename, 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    
bits = []
for photo in lines:
    bits.append(photo.split('_photo.jpg')[0])

fin_list = []
for txt in bits:
    fin_list.append(txt + '_info.txt')
    
for i in fin_list:
    print(i)
