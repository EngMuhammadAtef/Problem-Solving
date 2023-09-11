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