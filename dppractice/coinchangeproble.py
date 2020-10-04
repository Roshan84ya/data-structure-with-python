"""
Number of way to change a coin ie  if we have coin of 1 2 3 avaiable and we need a change of 4
hen we can have it in {1 1 1 1} {1 1 2 } {1,3} {2 2} in 4 ways

"""

for _ in range(int(input())):

    n= int(input())
    arr=list(map(int,input().split()))
    coin=int(input())

    dp=[0]*(coin+1)
    dp[0]=1

    for i in arr:
        for j in range(1,coin+1):
            if j>=i:                #if the curent vaue is greater of equal to the current value the we will add th bumber of way in current scenerio + number of way in the j-i scenerio
                dp[j]=dp[j]+dp[j-i]

    print(dp[-1])
