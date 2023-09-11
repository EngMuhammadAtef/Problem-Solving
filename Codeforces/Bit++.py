# Bit++
result = 0
for i in range(int(input())):
    op = input()
    if "+" in op:
        result += 1
    else:
        result -= 1
print(result)