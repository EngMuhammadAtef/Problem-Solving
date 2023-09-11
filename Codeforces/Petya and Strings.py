# Petya and Strings
s1 = input().upper()
s2 = input().upper()
result  = 0
for i in range(len(s1)):
    if  s1[i] > s2[i]:
        result = 1
        break
    elif s1[i] < s2[i]:
        result = -1
        break
print(result)