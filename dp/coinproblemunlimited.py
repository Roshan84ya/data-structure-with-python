def tnc(array,n):
    dp=[99999999]*(n+1) #here we intiallize the number of coin to greater than the maximum value
    
    dp[0]=0 #initialize the dp[0]=0 i.e when no value is reuired no coin is required

    for coin in array:
        for i in range(1,n+1):
            if (i>=coin):           #here we are calculating minimum number of oin to attain i value i.e for the i rupee i.e subproblem
                dp[i]=min(dp[i],1+dp[i-coin])
    return dp[value]


for _ in range(int(input())):
    value=int(input())                  #the value we wanted to attain
    noofcoin=int(input())               #the number of coin we have given denimination
    coinarray=list(map(int,input().split())) #the coin variety given
    k=tnc(coinarray,value)
    if k==99999999:
        print("Not possible")
    else:
        print(k)
