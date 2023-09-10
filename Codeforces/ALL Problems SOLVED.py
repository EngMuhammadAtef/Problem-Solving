########################################### ( My username on codeforces @MeMe. ) ###############################################
# Hit the Lottery
n = int(input())
dollar_bills = [100, 20, 10, 5, 1]
mini_bills = 0
 
for bill in dollar_bills:
    mini_bills += n // bill
    n %= bill
 
print(mini_bills)
################################################################################################################################
# Watermelon
n =  int(input())
print("YES") if n%2 == 0 and n !=2 else print("NO")
################################################################################################################################
# Way Too Long Words
for i in range(int(input())):
    word = input()
    print(f"{word[0]}{len(word)-2}{word[-1]}") if len(word) > 10 else print(f"{word}")
################################################################################################################################
# Team
n = int(input())
result = 0
for _ in range(n):
    team = list(map(int, input().split()))
    if team[0] == team[1] == 1 or team[1] == team[2] == 1 or team[0] == team[2] == 1:
        result += 1
print(result)
################################################################################################################################
# Theatre Square
from math import ceil
n,m,a = list(map(int,input().split()))
if a == 1:
    print(n * m)
else:
    s = ceil(n/a)
    d = ceil(m/a)
    print(s * d) 
################################################################################################################################
# Next Round
n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
res = 0
for i in range(n):
    if arr[i] >= arr[k-1] and arr[i] != 0:
        res += 1
print(res)
################################################################################################################################
# Domino piling
n, m = list(map(int, input().split()))
print(n*m//2)
################################################################################################################################
# Bit++
result = 0
for i in range(int(input())):
    op = input()
    if "+" in op:
        result += 1
    else:
        result -= 1
print(result)
################################################################################################################################
# Beautiful Matrix
found1row = 0
found1col = 0
for irow in range(1,6):
    row = list(map(int, input().split()))
    for ele in row:
        if ele == 1:
            found1row = irow
            found1col = row.index(ele) + 1
found1row = abs(3-found1row)
found1col = abs(3-found1col)
result = found1row + found1col 
print(result)
################################################################################################################################
# Petya and Strings
s1 = input().upper()
s2 = input().upper()
result  = 0
for i in range(len(s1)):
    if  s1[i] > s2[i]:
        result = 1
        break
    elif s1[i] < s2[i]:
        result = -1
        break
print(result)
################################################################################################################################
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
################################################################################################################################
# Word Capitalization
str = input().title()
print(str)
################################################################################################################################
# Boy or Girl
string = input() # wjmzbmr wjmzbr
string = sorted(string)
result = 1
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        result += 1
print("CHAT WITH HER!") if result % 2 == 0 else print("IGNORE HIM!")
################################################################################################################################
# String Task
str = input().lower()
result = ""
j = 0
for s in str:
    if s in "aoiuye":
        str = str.replace(s,"")

for i in range(len(str) * 2):
    if i&1 == 0:
        result += "."
    else:
        result += f"{str[j]}"
        j += 1
print(result)
################################################################################################################################
# Stones on the Table
n = int(input())
s = input()
count = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
print(count)
################################################################################################################################
# Bear and Big Brother
a, b = list(map(int, input().split()))
result = 0
while a <= b:
    a *= 3
    b *= 2
    result  += 1
print(result)
################################################################################################################################
# Soldier and Bananas
k,n,w = list(map(int,input().split()))
result = 0
for i in range(1,w+1):
    result += i*k
 
print( (result-n) if result > n else 0)
################################################################################################################################
# Elephant
pos = int(input())
count = 0
while pos >= 5:
    pos -= 5
    count += 1
while pos >= 4:
    pos -= 4
    count += 1
while pos >= 3:
    pos -= 3
    count += 1
while pos >= 2:
    pos -= 2
    count += 1
while pos >= 1:
    pos -= 1
    count += 1

print(count)
################################################################################################################################
# Word
word = input()
up_word = word.upper()
countupper, countlower = 0, 0

for i in range(len(word)):
    if word[i] == up_word[i]:
        countupper += 1
    else:
        countlower += 1
if countupper > countlower:
    print(word.upper())
else:
    print(word.lower())
################################################################################################################################
# Young Physicist
arr1,arr2,arr3 = [],[],[]
 
for _ in range(int(input())):
    x,y,z = list(map(int,input().split()))
    arr1.append(x)
    arr2.append(y)
    arr3.append(z)
 
i,j,k = sum(arr1), sum(arr2),sum(arr3)
print("YES" if i==j==k==0 else "NO")
################################################################################################################################
# Everything Everywhere All But One
for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print("YES" if sum(arr)/n in arr else "NO")
################################################################################################################################
# Wrong Subtraction
num,k = list(map(int,input().split()))
 
for i in range(k):
    num = str(num)
    if num[-1] == '0':
        num = num[:-1]
    else:
        num = int(num)
        num -= 1
print(num)
################################################################################################################################
# Football
pos = input()  # 00100110111111101
count = 1
isDen = "NO"
for i in range(len(pos)-1):
    if pos[i] != pos[i+1]: 
        count = 0
    count += 1
    if count >= 7:
        isDen = "YES"
 
print(isDen)
################################################################################################################################
# Anton and Danik
n = int(input())
caras = input().upper()
nA = 0
nD = 0
for c in caras:
    if c == "A":
        nA += 1
    elif c == "D":
        nD += 1
print("Anton") if nA > nD else print("Danik") if nD > nA else print("Friendship")
################################################################################################################################
# Tram
maxn = 0
temp = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    temp -= arr[0]
    temp += arr[1]
    maxn = temp if temp > maxn else maxn
 
print(maxn)
################################################################################################################################
# AvtoBus
for _ in range(int(input())):
    n=int(input())
    print(*([[(n+5)//6, n//4], [-1]][n%2|(n<4)]))
################################################################################################################################
# Translation
print("YES" if input() == input()[::-1] else "NO")
################################################################################################################################
# Night at the Museum
str = input() # zeus
result = 0
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(str)):
    if i == 0:
        if 26-letters.index(str[i])>letters.index(str[i]):
            result += letters.index(str[i])  
        else:
            result += 26-letters.index(str[i])
    else:
        if abs(letters.index(str[i])-letters.index(str[i-1])) < 26-abs(letters.index(str[i])-letters.index(str[i-1])):
            result += abs(letters.index(str[i])-letters.index(str[i-1]))
        else:
            result += 26-abs(letters.index(str[i])-letters.index(str[i-1]))
 
print(result)
################################################################################################################################
# Vanya and Fence
n, h = list(map(int, input().split()))
hights = list(map(int, input().split()))
width = 0
for high in hights:
    if high <= h:
        width += 1
    else:
        width += 2
print(width)
################################################################################################################################
# Beautiful Year
y = str(int(input())+1)
while y[0] in y[1:] or y[1] in y[2:] or y[2] == y[3]:
    y = str(int(y) + 1)
print(y)
################################################################################################################################
# Chat room
s = input()
hello = "hello"
 
for i in range(len(s)):
    if hello != "":
        if s[i] == hello[0]:
            hello = hello[1:]
 
print("YES" if hello == "" else "NO")
################################################################################################################################
# Lucky Division
n = int(input())
res = "NO"
arr = [4, 7, 47, 74, 447, 477, 744, 774, 747, 474]
 
for e in arr:
    if n in arr or n//e==n/e:
        res = "YES"
 
print(res)
################################################################################################################################
# Magnets
n = int(input())
arr = []
result = 1
for i in range(n):
    num = int(input())
    if len(arr) == 0:
        arr.append(num)
    else:
        if num != arr[-1]:
            arr.append(num)
            result += 1
print(result)
################################################################################################################################
# Is your horseshoe on the other hoof?
arr = [int(x) for x in input().split()]
counts = []
 
for i in range(len(arr)):
    count_num = arr[i:].count(arr[i])
    if count_num>1 and arr[i] not in arr[:i]:
        counts.append(count_num-1)
 
print(sum(counts))
################################################################################################################################
# Gravity Flip
n = int(input())
arr = list(map(int, input().split()))
for a in range(len(arr)): # Bubble sort
    for b in range(len(arr)-1):
        if arr[b] > arr[b+1]:
            arr[b], arr[b+1] = arr[b+1], arr[b]
print(*arr)
################################################################################################################################
# Registration system
n = int(input())
dic = {}
 
for i in range(n): # abbb ab ab
    st = input()
    
    if dic.setdefault(st,0):
        print(st+str(dic[st]))
    else:
        print("OK")
 
    dic[st] += 1
################################################################################################################################
# Police Recruits
n = int(input())
nums = list(map(int, input().split()))
count = 0
result = 0
# 1 -1 2 -1 -1 
for i in range(len(nums)):
    if nums[i] > 0:
        count += nums[i]
    else:
        if count == 0:
            result += 1
        else:
            count += nums[i]
print(result)
################################################################################################################################
# Sereja and Dima
n = int(input())
arr = list(map(int, input().split()))
start, end = 0, len(arr)-1
Ser, Dima = 0, 0
turn = 'Sereja'
# 2 4 3 5 >>>> 9 5
while start <= end:
    if arr[start] > arr[end]:
        if turn == 'Sereja':
            Ser += arr[start]
            start += 1
            turn = 'Dima'
        else:
            Dima += arr[start]
            start += 1
            turn = 'Sereja'
    else:
        if turn == 'Sereja':
            Ser += arr[end]
            end -= 1
            turn = 'Dima'
        else:
            Dima += arr[end]
            end -= 1
            turn = 'Sereja'
print(Ser, Dima)
################################################################################################################################
# Black Square
arr = list(map(int, input().split()))
str = input()
result = 0
for i in str:
    result += arr[int(i)-1]
print(result)
################################################################################################################################
# Codeforces Checking
for i in range(int(input())):
    print("YES") if input() in "codeforces" else print("NO")
################################################################################################################################
# Immobile Knight
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if x==1 or y==1:
        print(x, y)
    else:
        print(x-1,2)
################################################################################################################################
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
################################################################################################################################
# Mr. Perfectly Fine
for _ in range(int(input())):
    vict = {"left":10**6, "right":10**6, "two":10**6}
    for _ in range(int(input())):
        minu, aq_skill = input().split()
        if aq_skill[0] == "1" and aq_skill[1] == "1":
            vict["two"] = int(minu) if vict["two"] > int(minu) else vict["two"]
        if aq_skill[0] == "1":
            vict["left"] = int(minu) if vict["left"] > int(minu) else vict["left"]
        elif aq_skill[1] == "1":
            vict["right"] = int(minu) if vict["right"] > int(minu) else vict["right"]
 
    if vict["two"]!=10**6 and vict["two"] < (vict["left"]+vict["right"]):
        print(vict["two"])
    else:
        print(vict["left"]+vict["right"]) if (vict["left"]+vict["right"]) < 10**6 else print(-1)
################################################################################################################################
# Blank Space
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count_Zeros = 0
    res = []
    for i in range(len(arr)):
        if arr[i] == 0:
            count_Zeros += 1
        else:
            count_Zeros = 0
        res.append(count_Zeros)
    print(max(res))
################################################################################################################################
# Love Story
for _ in range(int(input())):
    s = input()
    codeforces = "codeforces"
    res = 0
    for i, j in zip(s, codeforces):
        if i!=j:
            res += 1
    print(res)
################################################################################################################################
# Exponential Equation
for _ in range(int(input())):
    n = int(input())
    print(-1) if n%2==1 else print(1, n//2)
################################################################################################################################
# Vanya and Cubes
n = int(input())
n_level = 0
count = 0
 
while n-(n_level+count) > 0:
    n_level += count+1
    n -= n_level
    count += 1
print(count)
################################################################################################################################
# Queue
n = int(input())
arr = list(map(int,input().split()))
sotred_arr = sorted(arr)
res = 0
time = 0
for i in range(len(sotred_arr)):
    if time <= sotred_arr[i]:
        res += 1
        time += sotred_arr[i]

print(res)
################################################################################################################################
# Following Directions
for _ in range(int(input())):
    n = int(input())
    word = input()
    res = "NO"
    r = [0,0]
    for i in range(n):
        if word[i] == "U":
            r[1] += 1
        elif word[i] == "D":
            r[1] -= 1
        elif word[i] == "R":
            r[0] += 1
        elif word[i] == "L":
            r[0] -= 1
        if r == [1,1]:
            res = 'YES'
        
    print(res)
################################################################################################################################
# Prepend and Append
for _ in range(int(input())):
    n = int(input())
    word = input()
    count = n
    for i,j in zip(range(n), range(n-1,-1,-1)):
        if i < j:
            if word[i] != word[j]:
                count -= 2
            else:
                break
    print(count)
################################################################################################################################
# New Palindrome
for _ in range(int(input())):
    s = input()
    res = "NO"
    for i in range(len(s)//2 -1):
        if s[i]!=s[i+1]: res = "YES"
    print(res)
################################################################################################################################
# Polycarp Writes a String from Memory

for _ in range(int(input())):
    s = input()
    h = set()
    res = 0
    for i in range(len(s)): # lollipops
        if len(h) >= 3 and s[i] not in h:
            res += 1
            h = set()
 
        h.add(s[i])
 
    print(res if len(h)==0 else res+1)
################################################################################################################################
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

