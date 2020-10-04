#maximum difference in an array

a=list(map(int,input().split()))
minv=a[0]
maxd=a[1]-a[0]
for i in range(1,len(a)):
    if maxd<a[i]-minv:
        maxd=a[i]-minv
    if minv>a[i]:
        minv=a[i]
print(maxd)

