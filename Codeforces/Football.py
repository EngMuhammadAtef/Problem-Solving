# Football
pos = input()  # 00100110111111101
count = 1
isDen = "NO"
for i in range(len(pos)-1):
    if pos[i] != pos[i+1]: 
        count = 0
    count += 1
    if count >= 7:
        isDen = "YES"
 
print(isDen)