'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def binarysearch(arr,l,r,k):
    if l<=r:
        mid=(l+r)//2
        if arr[mid]==k:
            return mid+1
        elif arr[mid]>k:
            return binarysearch(arr,l,mid-1,k)
        elif arr[mid]<k:
            return binarysearch(arr,mid+1,r,k)
    else:
        return -1

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

nm=int(input())
for i in range(nm):
    k=int(input())
    print(binarysearch(arr,0,n,k))

