def root(a):
    while arr[a]!=a:
        arr[a]=arr[arr[a]]
        a=arr[a]
    return a
def union1(a,b):
    roota=root(a)
    rootb=root(b)
    if roota==rootb:
        return
    if roota>rootb:
        arr[rootb]=roota
        
    else:
        arr[roota]=rootb
       
    
def fight(a,b):
    roota=root(a)
    rootb=root(b)
    if roota==rootb:
        return "TIE"
    
    if roota>rootb:
        return str(a+1)
    
    else:
        return str(b+1)
    
n,m=map(int,input().split())
arr=[i for i in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    union1(a-1,b-1)
  

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(fight(a-1,b-1))
