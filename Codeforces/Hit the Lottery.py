# Hit the Lottery
n = int(input())
dollar_bills = [100, 20, 10, 5, 1]
mini_bills = 0
 
for bill in dollar_bills:
    mini_bills += n // bill
    n %= bill
 
print(mini_bills)
