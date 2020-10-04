#stickler_theif_problem
#the probelm statement is their is a theif who cannot loot from two cosecutive house and you are hire
#to maximize his loot

""" input format
    Testcases
    number of house
    loot in the house

    output:-
    ans


    """


def theif(arr,n):
    if n==0:                                    #here if he has no house for loot then his maximum loot will be 0
        return 0
    if n==1:                                    # here if their has only one house then he can loot only one house and the loot in the house is our answer
        return arr[0]
    if n==2:                                    #here if we hace two house then we can have maximum loot from the two house and it is given by max(a[0],a[1])
        return max(arr[0],arr[1])

    
                                                #our main concept start from here if we take a house then we need to chose the maximum from the house that is next to next
                                                #house to end and if we don't take the hosue then we need to take
                                                #the house that are next to last i.e
                                                """  1,2,3,4,5,6,7,8   if we take 1 then we need to maximize the loot in 3,4,5,6,7,8 and if we don't take the 1 then we need to maimize
                                               from 2,3,4,5,6,7,8 similarly we can do this and further we can divide it into more subproblems"""
    dp=[0]*n                    
    dp[0]=a[0]
    dp[1]=max(a[0],a[1])

    for i in range(2,n):
        dp[i]=max(a[i]+dp[i-2],dp[i-1])         #here 1,2,3 if we are taking 2 then we cannot take 1 and 3 and if we take 3 then we can take 1 we cannot 2 so we have the maximum loot is 4
    return dp[-1]

    
    
n=int(input())
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    theif(arr,n)
