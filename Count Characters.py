#input the string from the user
s = input()

#find the first character
ch = s[0]

#declare and initialize the variable
countChar = 0

#for loop to iterate through the input string except the first character
for i in range(1, len(s)):
    
    #check if character matches with the first character
    if ch==s[i]:
        countChar = countChar + 1

#display the result on the computer screen.
if countChar == 1:
    print(countChar,ch)
else:
    print(countChar, " ",ch,"'s", sep="")
