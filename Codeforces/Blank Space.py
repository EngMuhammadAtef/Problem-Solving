# Blank Space
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count_Zeros = 0
    res = []
    for i in range(len(arr)):
        if arr[i] == 0:
            count_Zeros += 1
        else:
            count_Zeros = 0
        res.append(count_Zeros)
    print(max(res))