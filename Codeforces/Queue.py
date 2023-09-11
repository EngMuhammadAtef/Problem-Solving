# Queue
n = int(input())
arr = list(map(int,input().split()))
sotred_arr = sorted(arr)
res = 0
time = 0
for i in range(len(sotred_arr)):
    if time <= sotred_arr[i]:
        res += 1
        time += sotred_arr[i]

print(res)