# Likes
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    p = n = 0
    for i in arr:
        if i>0:
            p+=1
        else:
            n+=1
 
    arr1 = []
    arr2 = []
 
    for i in range(1,p+1):
        arr1.append(i)
    for i in range(p-1,p-n-1,-1):
        arr1.append(i)
    
    for o in [1,0]*n:
        arr2.append(o)
    for i in range(1,p-n+1):
        arr2.append(i)
    
    print(*arr1)
    print(*arr2)