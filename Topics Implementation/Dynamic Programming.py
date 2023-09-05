# Dynamic Programming Patterns
def knapsake():
    weights = [10, 4, 20, 5, 7]
    benfits = [10, 15, 3, 1, 4] # 0 1 0 0 1 ==>> 15 + 4 = 19
    sizeofBAG = 12
    def maxBenfits(i, reminder):
        if i == len(weights):
            return 0
        
        choice1 = maxBenfits(i+1, reminder)
        choice2 = 0
        
        if reminder >= weights[i]:
            choice2 = maxBenfits(i+1, reminder-weights[i]) + benfits[i]
        
        return max(choice1,choice2)

    print(maxBenfits(0,sizeofBAG))

def LCS():
    # a-s-df & adf = "adf" ==>> 3
    str1 = "asdf"
    str2 = "adf"

    def LCS(i, j):
        if i == len(str1) or j == len(str2):
            return 0
        
        if str1[i] == str2[j]:
            return LCS(i+1, j+1) + 1

        choice1 = LCS(i+1, j)
        choice2 = LCS(i, j+1)

        return max(choice1, choice2)

    print(LCS(0,0))

def maxPathGRID():
    # 567
    # 498
    # 321
    # [[5,1,2],
    # [6,7,8],
    # [1,4,9]]
    grid = [[5,1,2],
            [6,7,8],
            [1,4,9]]

    memo = [[-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1]] 

    def maxGRID(i, j):
        if i == len(grid) or j == len(grid):
            return 0
        
        if i == len(grid)-1 and j == len(grid)-1:
            return grid[i][j]
        
        if memo[i][j] != -1:
            return memo[i][j]

        choice1 = maxGRID(i, j+1) 
        choice2 = maxGRID(i+1, j)

        memo[i][j] = grid[i][j] + max(choice1, choice2)
        
        return memo[i][j]


    print(maxGRID(0,0))



