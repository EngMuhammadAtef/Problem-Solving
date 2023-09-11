# Police Recruits
n = int(input())
nums = list(map(int, input().split()))
count = 0
result = 0

for i in range(len(nums)):
    if nums[i] > 0:
        count += nums[i]
    else:
        if count == 0:
            result += 1
        else:
            count += nums[i]
print(result)