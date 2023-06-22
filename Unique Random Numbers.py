import random

def unique_random_ints(how_many, max_num):
    master_list = []
    i = 0
    retries = 0
    
    while i < how_many:
        n = random.randint(0, max_num)
        
        if n not in master_list:
            master_list.append(n)
            i += 1
            
        else:
            retries += 1
    
    for x in master_list:
        print(x, end = ' ')
        
    print('retries='+str(retries))
    
    return master_list

if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    random.seed(seed)
    
    unique_random_ints(how_many, max_num)
