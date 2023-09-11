# Beautiful Year
y = str(int(input())+1)
while y[0] in y[1:] or y[1] in y[2:] or y[2] == y[3]:
    y = str(int(y) + 1)
print(y)