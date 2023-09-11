# Elephant
pos = int(input())
count = 0
while pos >= 5:
    pos -= 5
    count += 1
while pos >= 4:
    pos -= 4
    count += 1
while pos >= 3:
    pos -= 3
    count += 1
while pos >= 2:
    pos -= 2
    count += 1
while pos >= 1:
    pos -= 1
    count += 1

print(count)