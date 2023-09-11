# Love Story
for _ in range(int(input())):
    s = input()
    codeforces = "codeforces"
    res = 0
    for i, j in zip(s, codeforces):
        if i!=j:
            res += 1
    print(res)