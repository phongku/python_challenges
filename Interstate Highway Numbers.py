highway_number = int(input())
highway_type = ''
direction = ''

if highway_number == 0:
    print(f'{highway_number} is not a valid interstate highway number.')
    
if highway_number % 100 == 0 and highway_number != 0:
    print(f'{highway_number} is not a valid interstate highway number.')

if len(str(highway_number)) == 3:
    highway_type = 'auxiliary'
else:
    highway_type = 'primary'

if highway_number % 2 == 0 and highway_number != 0 and highway_number % 100 != 0:
    direction = 'east/west'
    if highway_type == 'primary':
        print(f'I-{highway_number} is {highway_type}, going {direction}.')
    else:
        print(f'I-{highway_number} is {highway_type}, serving I-{highway_number % 100}, going {direction}.')
elif highway_number % 2 == 1 and highway_number != 0 and highway_number % 100 != 0:
    direction = 'north/south'
    if highway_type == 'primary':
        print(f'I-{highway_number} is {highway_type}, going {direction}.')
    else:
        print(f'I-{highway_number} is {highway_type}, serving I-{highway_number % 100}, going {direction}.')

    
