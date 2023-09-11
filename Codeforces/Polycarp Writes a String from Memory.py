# Polycarp Writes a String from Memory
for _ in range(int(input())):
    s = input()
    h = set()
    res = 0
    for i in range(len(s)): # lollipops
        if len(h) >= 3 and s[i] not in h:
            res += 1
            h = set()
        h.add(s[i])
 
    print(res if len(h)==0 else res+1)