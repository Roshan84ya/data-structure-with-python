#searching element in sorted array
def bsearch(arr,n,s,e):
    if s<=e:
        mid=(s+e)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            return bsearch(arr,n,mid+1,e)
        elif arr[mid]>n:
            return bsearch(arr,n,s,mid-1)
    else:
        return -2
    


a=[1,2,3,4,5,6,7,8,9]
n=1
print("The element is found at {} position".format(bsearch(a,n,0,len(a)-1)+1))
