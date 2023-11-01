
def knapSackRec(n, W, wt, profit): 

    if n == 0 or W == 0: 
        return 0


    if wt[n-1] <= W: 
        return max(profit[n-1] + knapSackRec(n-1, W - wt[n-1], wt, profit),
                   knapSackRec(n-1, W, wt, profit))
    else: 
        return knapSackRec(n-1, W, wt, profit)

def knapSackMem(n, W, wt, profit,t):
    
    if n == 0 or W == 0:
        return 0;
    
    if t[n][W] != -1:
        return t[n][W]
    
    if wt[n-1] <= W:
        t[n][W] = max(profit[n-1] + knapSackMem(n-1, W - wt[n-1], wt, profit,t),
                    knapSackMem(n-1, W, wt, profit,t))
        return t[n][W]
    else:
        t[n][W] = knapSackMem(n-1, W, wt, profit,t)
        return t[n][W]
    
def knapSackTab(n, W, wt, profit):
    dp=[[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    for i in range(n + 1):
        for j in range(W + 1):
            if i==0 or j==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
                dp[i][j]=max(profit[i-1] + dp[i-1][j - wt[i-1]],
                             dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]

    return dp[n][W]


def main():
    profit = [60,170, 100, 120] 
    weight = [10,40, 20, 30] 
    W = 50
    n = len(profit)

# n = int(input("Enter the number of items: "))
# profit=[]
# weight=[]

# for i in range(n):
#     item_profit=int(input(f"Enter profit for item {i + 1}: "))
#     item_weight=int(input(f"Enter weight for item {i + 1}: "))
#     profit.append(item_profit)
#     weight.append(item_weight)

    print(f"Recursive: {knapSackRec(n,W,weight,profit)}") #TC:O(2^N) SC:O(N)

    # Top Down
    t = [[-1 for x in range(W + 1)] for y in range(n + 1)]
    print(f"Memoized Solution: {knapSackMem(n, W, weight, profit,t)}") # TC:O(N*W) SC:O(N*W)+O(N)

    #Bottom Up
    print(f"Tabulation: {knapSackTab(n,W,weight,profit)}") #TC:O(N*W) SC:O(N*W)
    
if __name__ == '__main__': 
    main()
