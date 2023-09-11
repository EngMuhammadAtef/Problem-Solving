# Lucky Division
n = int(input())
res = "NO"
arr = [4, 7, 47, 74, 447, 477, 744, 774, 747, 474]
 
for e in arr:
    if n in arr or n//e==n/e:
        res = "YES"
 
print(res)