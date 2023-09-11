# Chat room
s = input()
hello = "hello"
 
for i in range(len(s)):
    if hello != "":
        if s[i] == hello[0]:
            hello = hello[1:]
 
print("YES" if hello == "" else "NO")