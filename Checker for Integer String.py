user_string = input()

def check_integer(string):
    for char in string:
        if not char.isdigit():
            return "No"
    return "Yes"

result = check_integer(user_string)
print(result)
