a=[1,2,3,4,5,6,7]
b=[3,5]
k=[]
i=0
j=0
while i<len(a) or j <len(b):
    if i==len(a):
        k=k+b[j:]
        j=len(b)
    elif j==len(b):
        k=k+a[i:]
        i=len(a)
    elif a[i]<=b[j]:
        k.append(a[i])
        i+=1
    elif b[j]<a[i]:
        k.append(b[j])
        j+=1




    
