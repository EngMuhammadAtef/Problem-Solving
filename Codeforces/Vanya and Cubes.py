# Vanya and Cubes
n = int(input())
n_level = 0
count = 0
 
while n-(n_level+count) > 0:
    n_level += count+1
    n -= n_level
    count += 1
print(count)