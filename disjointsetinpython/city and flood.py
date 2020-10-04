def invade(i,j):
    if fatland[j]==-1:
        return
    else:
        fatland[j]=-1
    
n=int(input())
fatland=[i for i in range(n)]
for _ in range(int(input())):
    i,j=map(int,input().split()) #i will attack the j and rename it to j
    invade(i-1,j-1)
count=0
for i in fatland:
    if (i!=-1):
        count+=1
print(count)
