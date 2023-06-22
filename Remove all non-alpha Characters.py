question = input()

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

newlist = [i for i in question if i in alph]

output = ''.join(newlist)

print(output)
