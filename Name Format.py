full_name = input()

name_list = full_name.split()

if len(name_list) == 3:
    print(f'{name_list[-1]}, {name_list[0][0]}.{name_list[1][0]}.')
else:
    print(f'{name_list[-1]}, {name_list[0][0]}.')
