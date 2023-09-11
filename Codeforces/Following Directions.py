# Following Directions
for _ in range(int(input())):
    n = int(input())
    word = input()
    res = "NO"
    r = [0,0]
    for i in range(n):
        if word[i] == "U":
            r[1] += 1
        elif word[i] == "D":
            r[1] -= 1
        elif word[i] == "R":
            r[0] += 1
        elif word[i] == "L":
            r[0] -= 1
        if r == [1,1]:
            res = 'YES'
        
    print(res)