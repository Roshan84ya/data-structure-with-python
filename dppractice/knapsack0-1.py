def findmaxm(n,wt,v,w):
    dp=[0]*(n+1)
    for i in range(n+1):
        dp[i]=[0]*(wt+1)

    for i in range(1,n+1):
        for j in range(1,wt+1):
            if j<w[i-1]: #if the curent weight in the knapsack is smalle then the current weight then we cant include that weight
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(v[i-1]+dp[i-1][j-w[i-1]],dp[i-1][j])
    return dp[-1][-1]

for _ in range(int(input())):
    n=int(input())
    wt=int(input())
    v=list(map(int,input().split()))
    w=list(map(int,input().split()))
    print(findmaxm(n,wt,v,w))
