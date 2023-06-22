def print_all_permutations(permList, nameList):
    if len(nameList) == 0:
        print(', '.join(permList))
    else:
        for i in range(len(nameList)):
            newPerm = permList + [nameList[i]]
            newNameList = nameList[:i] + nameList[i+1:]
            print_all_permutations(newPerm, newNameList)

if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList)
