
def segmenttree(a,s,end,index): #here it looks more clear s=start index end index and index is the current index of the segment tree where we want to put the requires thing that is asked by the question
    
    if s==end:
        arr[index]=a[s]
        return
            
            
            
    else:
        mid=(s+end)//2          #here we divide our tree into two parts that is right part and the left part on the basis of mid that is we found out the mid point of the index and then
                                # we build the segment tree for the left part where start to mid and that elemnt will have the root node at 2*index
        segmenttree(a,s,mid,2*index)
        segmenttree(a,mid+1,end,(2*index)+1)#similarly for the right nof=de we have the element from the mid+1 to the end and their index will be 2*index +1
            
        arr[index]=arr[2*index]+arr[2*index +1] # when we calclate all the child node we put the addition of the child node into their root node
            
            
    
            
        
    
    

a=[10,20,30,40,50,60]#number of element in the array is st
st=len(a)

arr=[0]*(4*st)      #number of element and the nodes in the segment tree is 4n (n=total number of the element in our array)
segmenttree(a,0,5,1)#here our first argument is a that is our array foe which we are trying to build the segment tree 0 is the starting index of array and 5 is the end index and 1 is the index
                    #index of segment tree from where we are start filling these things
print(*arr)
