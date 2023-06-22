input_month = input()
input_day = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if (input_month not in months) or (input_day <= 0) or (input_day > 31) or (input_month + str(input_day) == 'September31'):
    print('Invalid')
elif input_month == 'March':
    if input_day <= 19:
        print('Winter')
    else:
        print('Spring')
elif input_month == 'April' or input_month == 'May':
    print('Spring')
elif input_month == 'June':
    if input_day <= 20:
        print('Spring')
    else:
        print('Summer')
elif input_month == 'July' or input_month == 'August':
    print('Summer')
elif input_month == 'September':
    if input_day <= 21:
        print('Summer')
    else:
        print('Autumn')
elif input_month == 'October' or input_month == 'November':
    print('Autumn')
elif input_month == 'December':
    if input_day <= 20:
        print('Autumn')
    else:
        print('Winter')
elif input_month == 'January' or input_month == 'February':
    print('Winter')
