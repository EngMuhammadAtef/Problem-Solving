# Theatre Square
from math import ceil
n,m,a = list(map(int,input().split()))
if a == 1:
    print(n * m)
else:
    s = ceil(n/a)
    d = ceil(m/a)
    print(s * d) 