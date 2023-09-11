# AvtoBus
for _ in range(int(input())):
    n=int(input())
    print(*([[(n+5)//6, n//4], [-1]][n%2|(n<4)]))