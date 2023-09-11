# Wrong Subtraction
num,k = list(map(int,input().split()))
 
for i in range(k):
    num = str(num)
    if num[-1] == '0':
        num = num[:-1]
    else:
        num = int(num)
        num -= 1
print(num)