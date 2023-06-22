stringa = input()
param = input()

stringa = stringa.split()
stringb = [int(i) for i in stringa]

param = param.split()
paramb = [int(i) for i in param]

small = paramb[0]
large = paramb[1]

result = [i for i in stringb if small <= i <= large]

for i in result:
    print(i, end=',')
