# Helpful Maths
str = input()
nums = []
result = ""
for i in range(0,len(str),2):
    nums.append(int(str[i]))

while len(nums) != 0:
    mn = min(nums)
    result += f"{mn}"
    if len(nums) > 1:
        result += "+"
    nums.remove(mn)

print(result)