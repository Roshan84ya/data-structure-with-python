"""
find the number of way to rach at the stair using steps 1,2,3

"""

for _ in range(int(input())):

    n=int(input())
    dp=[0]*(n)

    
    if n>=1:   #here e have the base case if we wanted to go on stair 1st we can go only in 1 way
        dp[0]=1
        
    if n>=2: # if we wanted to go on the stair number 2 then we can go with 1 1 and 2 only that is by 2 ways
        dp[1]=2
        
    if n>=3:        # if we wanted to go on the staor number 3 we can go by 1 1 1 and 1 2 and 2 1 and 3 here we have 4 ways
    
        
        
        dp[2]=4  
        for i in range(3,n):                 
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    
    print(dp[n-1])


"""
approach if we wanted to go on step number 4
then we need to calculated in how many ways we can go there by using skipping step 1 or step 2 or step3 i.e
we break it into

                                                         4
                                    4-3             + 4-2 +                  4-1
                        (1-3) +(1-2) +(1-1)     (2-3)+2-2 2-1              3-3  3-2  3-1
                          -2    -1      0        -1    0   1                0    1    2

similary the tree will goes on till we reach at the base case i.e if -ve then we can go in any way so 0 but if 0 then the
in this way we are calculating the total number way by skipping 1 2 3 steps we an reach to the n step i.e to reach at 4 the toal number of ways we reac at 3 + 2 + 1 


"""
