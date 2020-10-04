def buildsegmenttree(arr,s,end,index):
    if s==end:
        tree[index]=arr[s]
        return
    mid=(s+end)//2
    buildsegmenttree(arr,s,mid,2*index)
    buildsegmenttree(arr,mid+1,end,2*index +1)
    tree[index]=tree[2*index]+tree[2*index +1]

def summquery(arr,s,end,index,a,b):
    if end<a or s>b:
        return 0
    if a<=s and b>=end:
        
        return tree[index]
    mid=(s+end)//2
    return summquery(arr,s,mid,2*index,a,b)+summquery(arr,mid+1,end,2*index +1 ,a,b)

    
    


arr=[10,20,30,40]

tree=[0]*(4*len(arr))
buildsegmenttree(arr,0,3,1)
print(*tree)
a,b=map(int,input().split())
print(summquery(arr,0,len(arr)-1,1,a,b))
