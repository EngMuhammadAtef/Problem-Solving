# Kuriyama Mirai's Stones
def getResult(q,S,E):
    if q == 1:
        arr = sums
        if S == 1:
            result = arr[E-1]
        else:
            result = arr[E-1] - arr[S-2]
    else:
        arr = SortedSums
        if S == 1:
            result = arr[E-1]
        else:
            result = arr[E-1] - arr[S-2]
    return result

NCosts = int(input())
costs = list(map(int, input().split()))
n = int(input())
Sortedcosts = sorted(costs)
results = []
sums = []
SortedSums = []
 
for i in range(len(costs)):
    if i == 0 :
        sums.append(costs[0])
    else:
        sm = sums[i-1] + costs[i]
        sums.append(sm)
 
 
for i in range(len(Sortedcosts)):
    if i == 0 :
        SortedSums.append(Sortedcosts[0])
    else:
        sm = SortedSums[i-1] + Sortedcosts[i]
        SortedSums.append(sm)
 
for _ in range(n):
    question = list(map(int, input().split())) 
    result = getResult(question[0],question[1],question[2])
    results.append(result)
 
for result in results:
    print(result)
