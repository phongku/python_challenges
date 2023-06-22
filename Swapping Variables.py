
def swap_values(user_val1,user_val2,user_val3,user_val4):
    temp1 = user_val1
    user_val1 = user_val2
    user_val2 = temp1
    temp2 = user_val3
    user_val3 = user_val4
    user_val4 = temp2
    return user_val1,user_val2,user_val3,user_val4
    

if __name__ == '__main__': 
    
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num1,num2,num3,num4 = swap_values(num1,num2,num3,num4)
    print(num1,num2,num3,num4)
    
