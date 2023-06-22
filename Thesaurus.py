synonyms = {}
inp2 = input()
inp = inp2  + '.txt'
letter = input()

with open(inp, 'r') as filename:
    lines = [line.strip().split() for line in filename]
    
full_list = []
for sublist in lines:
    for item in sublist:
        full_list.append(item)

master_list = []
for item in full_list:
    if item[0] == letter:
        master_list.append(item)
        
if master_list != []:
    for _ in master_list:
        print(_)
else:
    print(f'No synonyms for {inp2} begin with {letter}.')
