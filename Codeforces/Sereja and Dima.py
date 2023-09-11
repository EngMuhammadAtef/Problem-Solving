# Sereja and Dima
n = int(input())
arr = list(map(int, input().split()))
start, end = 0, len(arr)-1
Ser, Dima = 0, 0
turn = 'Sereja'
# 2 4 3 5 >>>> 9 5
while start <= end:
    if arr[start] > arr[end]:
        if turn == 'Sereja':
            Ser += arr[start]
            start += 1
            turn = 'Dima'
        else:
            Dima += arr[start]
            start += 1
            turn = 'Sereja'
    else:
        if turn == 'Sereja':
            Ser += arr[end]
            end -= 1
            turn = 'Dima'
        else:
            Dima += arr[end]
            end -= 1
            turn = 'Sereja'
print(Ser, Dima)