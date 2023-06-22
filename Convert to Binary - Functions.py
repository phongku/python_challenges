def int_to_reverse_binary(integer_value):
    binary_string = ""
    while integer_value > 0:
        binary_string += str(integer_value % 2)
        integer_value //= 2
    return binary_string

def string_reverse(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    integer_value = int(input(""))
    binary_string = int_to_reverse_binary(integer_value)
    reversed_string = string_reverse(binary_string)
    print(reversed_string)

