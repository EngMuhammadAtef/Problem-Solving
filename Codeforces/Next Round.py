# Next Round
n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
res = 0
for i in range(n):
    if arr[i] >= arr[k-1] and arr[i] != 0:
        res += 1
print(res)