n = int(input())

val = []

for i in range(n):
    val.append(float(input()))

for i in range(n):
    your_value = val[i]/max(val)
    print('{:.2f}'.format(your_value)) 
