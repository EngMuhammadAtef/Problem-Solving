# Anton and Danik
n = int(input())
caras = input().upper()
nA = 0
nD = 0
for c in caras:
    if c == "A":
        nA += 1
    elif c == "D":
        nD += 1
print("Anton") if nA > nD else print("Danik") if nD > nA else print("Friendship")