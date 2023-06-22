money = int(input())

if money <= 0:
    print('No change')

Dollars = money // 100
money = money % 100

Quarters = money // 25
money = money % 25

Dimes = money // 10
money = money % 10

Nickels = money // 5
Pennies = money % 5

if Dollars > 1:
    print(f'{Dollars} Dollars')
elif Dollars == 1:
    print(f'{Dollars} Dollar')
    
if Quarters > 1:
    print(f'{Quarters} Quarters')
elif Quarters == 1:
    print(f'{Quarters} Quarter')
    
if Dimes > 1:
    print(f'{Dimes} Dimes')
elif Dimes == 1:
    print(f'{Dimes} Dime')
    
if Nickels > 1:
    print(f'{Nickels} Nickels')
elif Nickels == 1:
    print(f'{Nickels} Nickel')

if Pennies > 1:
    print(f'{Pennies} Pennies')
elif Pennies == 1:
    print(f'{Pennies} Penny')
