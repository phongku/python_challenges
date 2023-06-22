def mad_libs():
    while True:
        user_input = input()
        words = user_input.split()
        
        if words[0] == 'quit':
            break
        
        word = words[0]
        number = int(words[1])
        
        print(f'Eating {number} {word} a day keeps you happy and healthy.')
        
mad_libs()
