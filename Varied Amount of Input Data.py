from statistics import mean

stringa = input()

stringa = stringa.split()
stringa = [float(i) for i in stringa]
stringa.sort()

print(f'{stringa[-1]:.2f} {mean(stringa):.2f}')
