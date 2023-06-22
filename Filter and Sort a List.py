stringa = input()

stringa = stringa.split()
lista = [int(i) for i in stringa]

listb = [i for i in lista if i < 0]

listb.sort(reverse = True)

print(*listb, end = ' ')
