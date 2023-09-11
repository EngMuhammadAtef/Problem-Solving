# Bear and Big Brother
a, b = list(map(int, input().split()))
result = 0
while a <= b:
    a *= 3
    b *= 2
    result  += 1
print(result)