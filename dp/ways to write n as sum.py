"""
                Way to write n as sum
    Given an positive integer N, the task is to find the number of different
    ways in which N cabnbe written as a sum of two or more positive integer

    Input Format:-
    T= Test case
    N=integer
    output format:-
    Number of ways N can be written as the sum of two or more positive integer
    for each test modulo 10^9

"""
def countWays(n):
    arr=[0]*(n+1)
    arr[0]=1
    for i in range(1,n):
        for j in range(1,n+1):
            if j>=i:
                arr[j]=arr[j]+arr[j-i]
    return arr[-1]


"""

lets take the example of 5
firstly we can write it as
-->1+1+1+1+1
but if i have one more coin of other type 2 the we can aslo achieve the sum which is greater than or equal to 2
like

"""

t=int(input())

for i in range(t):
    n=int(input())
    print(countWays(n))
    
