def reverse_binary(x):
    reverse_binary_str = ''
    while x > 0:
        reverse_binary_str += str(x % 2)
        x //= 2
    return reverse_binary_str
    
x = int(input())

result = reverse_binary(x)

print(result)
