for i in range(int(input())):
    k=int(input())
    count=0
    
    while k!=0:
        mink=k
        if k>2:
            jk=k
            for j in range(2,(k//2)+1):
                if k%j==0:
                    if mink>abs(j-k//j):
                        mink=abs(j-k//j)
                        jk=max(j,k//j)
            
                   
        k=min(k-1,jk)
        print(k)
        count+=1
    print(count)
        

"""N = 79

moves = [0] + N * [N]

for i in range(N):
    moves[i+1] = min(moves[i+1], moves[i] + 1)
    j = 2
    while j <= i and j * i <= N:
        moves[i * j] = min(moves[i * j], moves[i] + 1)
        j += 1
    

for _ in range(int(input())):
    print(moves[int(input())])
    print(moves)"""
    
