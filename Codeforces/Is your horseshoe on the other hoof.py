# Is your horseshoe on the other hoof?
arr = [int(x) for x in input().split()]
counts = []
 
for i in range(len(arr)):
    count_num = arr[i:].count(arr[i])
    if count_num>1 and arr[i] not in arr[:i]:
        counts.append(count_num-1)
 
print(sum(counts))