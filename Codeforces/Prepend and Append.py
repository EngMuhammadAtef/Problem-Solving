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