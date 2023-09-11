# Soldier and Bananas
k,n,w = list(map(int,input().split()))
result = 0
for i in range(1,w+1):
    result += i*k
 
print( (result-n) if result > n else 0)