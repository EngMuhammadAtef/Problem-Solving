# Young Physicist
arr1,arr2,arr3 = [],[],[]
 
for _ in range(int(input())):
    x,y,z = list(map(int,input().split()))
    arr1.append(x)
    arr2.append(y)
    arr3.append(z)
 
i,j,k = sum(arr1), sum(arr2),sum(arr3)
print("YES" if i==j==k==0 else "NO")