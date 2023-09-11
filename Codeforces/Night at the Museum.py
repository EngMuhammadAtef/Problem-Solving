# Night at the Museum
str = input() # zeus
result = 0
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(str)):
    if i == 0:
        if 26-letters.index(str[i])>letters.index(str[i]):
            result += letters.index(str[i])  
        else:
            result += 26-letters.index(str[i])
    else:
        if abs(letters.index(str[i])-letters.index(str[i-1])) < 26-abs(letters.index(str[i])-letters.index(str[i-1])):
            result += abs(letters.index(str[i])-letters.index(str[i-1]))
        else:
            result += 26-abs(letters.index(str[i])-letters.index(str[i-1]))
 
print(result)