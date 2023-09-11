# Beautiful Matrix
found1row = 0
found1col = 0
for irow in range(1,6):
    row = list(map(int, input().split()))
    for ele in row:
        if ele == 1:
            found1row = irow
            found1col = row.index(ele) + 1
found1row = abs(3-found1row)
found1col = abs(3-found1col)
result = found1row + found1col 
print(result)