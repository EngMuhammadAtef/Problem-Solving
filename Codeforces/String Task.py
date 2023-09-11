# String Task
str = input().lower()
result = ""
j = 0
for s in str:
    if s in "aoiuye":
        str = str.replace(s,"")

for i in range(len(str) * 2):
    if i&1 == 0:
        result += "."
    else:
        result += f"{str[j]}"
        j += 1
print(result)