def builttree(arr,s,end,index):
    if s==end:
        tree[index]=arr[s-1]
        return tree[index]
    mid=(s+end)//2
    builttree(arr,s,mid,2*index)
    builttree(arr,mid+1,end,2*index+1)
    tree[index]=min(tree[2*index],tree[2*index+1])

def getmin(a ,b , s , end , index):
    if a>end or s>b:
        return 999999
    if a<=s and b>=end:
        return tree[index]
    
            
    mid=(s+end)//2
    return min(getmin(a ,b , s , mid , 2*index),getmin(a ,b , mid+1 , end , 2*index +1))
    
def update(upidx, value , s, end , index):
    if s>upidx or end <upidx:
        return
    if s==end==upidx:
        tree[index]=value
        return tree[index]
    
    mid=(s+end)//2
    update(upidx, value , s, mid , 2*index)
    update(upidx, value , mid+1, end , 2*index +1)
    tree[index]=min(tree[2*index],tree[2*index+1])
    
        
    
    

m,n=map(int,input().split())
arr=list(map(int,input().split()))[:m]
tree=[0]*(4*m)
builttree(arr,1,m,1)
print(*tree)

for i in range(n):
    st=input().split()
    if st[0]=="q":
        print(getmin(int(st[1]),int(st[2]), 1,m, 1))
    elif st[0]=="u":
        update(int(st[1]),int(st[2]), 1, m ,1)
        print(*tree)
    
