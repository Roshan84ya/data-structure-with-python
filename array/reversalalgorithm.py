#rotation_by N

def leftrotate(a,n):
    reverse(a,0,n-1)
    reverse(a,n,len(a)-1)
    reverse(a,0,len(a)-1)
def reverse(a,i,h):
    while i<h:
        a[i],a[h]=a[h],a[i]
        i+=1
        h-=1

a=[1,2,3,4,5,6,7,8,9]
n=int(input())
k=leftrotate(a,n)
print(a)
