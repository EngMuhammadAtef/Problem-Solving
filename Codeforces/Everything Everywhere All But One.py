# Everything Everywhere All But One
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print("YES" if sum(arr)/n in arr else "NO")