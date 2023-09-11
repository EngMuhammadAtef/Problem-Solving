# Gravity Flip
n = int(input())
arr = list(map(int, input().split()))
for a in range(len(arr)): # Bubble sort
    for b in range(len(arr)-1):
        if arr[b] > arr[b+1]:
            arr[b], arr[b+1] = arr[b+1], arr[b]
print(*arr)