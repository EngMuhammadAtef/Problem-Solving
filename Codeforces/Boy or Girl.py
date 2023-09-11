# Boy or Girl
string = input() # wjmzbmr wjmzbr
string = sorted(string)
result = 1
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        result += 1
print("CHAT WITH HER!") if result % 2 == 0 else print("IGNORE HIM!")