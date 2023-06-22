while True:
    string = str(input())
    if string == 'Done' or string == 'done' or string == 'd':
        break
    else:
        print(string[::-1])
