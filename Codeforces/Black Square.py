# Black Square
arr = list(map(int, input().split()))
str = input()
result = 0
for i in str:
    result += arr[int(i)-1]
print(result)