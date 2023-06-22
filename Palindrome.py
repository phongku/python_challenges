question = input()
hold = question

question = question.replace(' ', '')
reverse = question [::-1]

if question == reverse:
    print(f'palindrome: {hold}')
else:
    print(f'not a palindrome: {hold}')
