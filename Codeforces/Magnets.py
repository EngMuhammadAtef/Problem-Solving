# Magnets
n = int(input())
arr = []
result = 1
for i in range(n):
    num = int(input())
    if len(arr) == 0:
        arr.append(num)
    else:
        if num != arr[-1]:
            arr.append(num)
            result += 1
print(result)