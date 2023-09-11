# New Palindrome
for _ in range(int(input())):
    s = input()
    res = "NO"
    for i in range(len(s)//2 -1):
        if s[i]!=s[i+1]: res = "YES"
    print(res)