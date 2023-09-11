# Tram
maxn = 0
temp = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    temp -= arr[0]
    temp += arr[1]
    maxn = temp if temp > maxn else maxn
 
print(maxn)