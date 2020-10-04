#building the segmenttree for the given array
"""
for building the segment tree we need to build the tree till we reach at the base condition that is when end ==start i.e the case when in out segment tree has only one element and that is
equal to the element at index i so in this manner we are firstly filling the element at the last index i.e from last to first

and if the index of parent node is =i then the index of its right node is 2*i and the index of its left node is 2*i +1
so we build the segmrnt tree y the recursive call we firsty find out the mid element
mid=(end+start)/2 and our left subtree will indicatr the element from start to mid and its index will be (2*i-->indexof parent node)
similarly for the right subtree will indicate the element from the mid+1 to the end and it sindex will be 2*index +1

"""
def buildtree(arr,s,end,index):
    if s==end:
        tree[index]=arr[s]
    else:
        mid=(s+end)//2
        buildtree(arr,s,mid,2*index)
        buildtree(arr,mid+1,end,2*index+1)
        tree[index]=tree[2*index]+tree[2*index +1]


#get sum in the range of a,b
"""
here we have three cases i.e if some element is partially inside the range of a,b then we break the element nto more smaller and we return the value when the give range is totally inside
our range of a,b i.e a<=s<=end<=b
if some element is not in the rrange of a,b i.e totally out of the range of the ab then we will just return 0 as we are not interested in finding the sum of that element
the condition for that is
if s>b(end of fired query) or a >end(end of our subarray)
"""
def getsum(a,b,s,end,index):
    if s>b or a>end:
        return 0
    elif a<=s and b>=end:
        return tree[index]
    mid=(s+end)//2
    return getsum(a,b,s,mid,2*index)+getsum(a,b,mid+1,end,2*index +1)

#updating value

"""
we update al the value that will fall in in which our uppdating index will fall i.e s<=i<=b
and if our index willl not fall in the range then we simply return
and we call our recursive function till we reach at the leaf node i.e till we have 1 element in the leaf node
"""
def update(s,end,upidx,diff,index):
    if end<upidx or s>upidx:
        return
    if s<=upidx<=end:
        tree[index]+=diff
    if end>s:
        mid=(s+end)//2
        update(s,mid,upidx,diff,2*index)
        update(mid+1 ,end,upidx,diff,2*index +1)


        


arr=[10,20,30,40] #arr for which we need to build the segment tree
tree=[0]*4*(len(arr))
#building the segment tree
buildtree(arr,0,len(arr)-1,1)
print(*tree)

               
#getsum range query
a,b=map(int,input().split())
print(getsum(a,b,0,len(arr)-1,1))

#update tree
uindex,value=map(int,input().split())
update(0 , len(arr)-1 ,uindex ,value-arr[uindex],1)
print(*tree)

#update tree
uindex,value=map(int,input().split())
update(0 , len(arr)-1 ,uindex ,value-arr[uindex],1)
print(*tree)

#getsum range query
a,b=map(int,input().split())
print(getsum(a,b,0,len(arr)-1,1))

#getsum range query
a,b=map(int,input().split())
print(getsum(a,b,0,len(arr)-1,1))

               


