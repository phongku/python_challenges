import math

x = float(input())
y = float(input())
z = float(input())

print(f'{x ** z:.2f} {x ** y ** z:.2f} {abs(x - y):.2f} {math.sqrt(x ** z):.2f}')
