# Vanya and Fence
n, h = list(map(int, input().split()))
hights = list(map(int, input().split()))
width = 0
for high in hights:
    if high <= h:
        width += 1
    else:
        width += 2
print(width)