# Immobile Knight
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if x==1 or y==1:
        print(x, y)
    else:
        print(x-1,2)