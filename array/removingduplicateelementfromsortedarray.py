a=[1,2,3,4,5,6]
i=0
while i<(len(a)-1):
    
    if a[i]==a[i+1]:
        del a[i+1]
    elif a[i]!=a[i+1]:
        i+=1
print(a)
