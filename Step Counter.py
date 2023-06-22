def feet_to_steps(num_feet):
    steps = int(num_feet / 2.5)
    return steps

if __name__ == '__main__':
    number_of_feet = float(input())
    number_of_steps = feet_to_steps(number_of_feet)
    print(number_of_steps)
