# Team
n = int(input())
result = 0
for _ in range(n):
    team = list(map(int, input().split()))
    if team[0] == team[1] == 1 or team[1] == team[2] == 1 or team[0] == team[2] == 1:
        result += 1
print(result)