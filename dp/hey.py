# 4
# 8 5 2 3
# 8 5 

print(fl)   
"""count=0
sum1=0
i=0
f=0
j=0
while j<len(kl):

    
    
    
    if kl[j]!=jk[i]:
        count+=1
        j+=1
    if kl[j]==jk[i]:
        count+=1
        sum1+=count
        count=0
        kl=kl[j+1:]+kl[:j]
        i+=1
        j=0
    
print(sum1,f)
        """




for i in range(len(kl)):
    k=min(kl)
    while k!=kl[0]:
        count+=1
        kl.append(kl.pop(0))
        print(kl)
    else:
        count+=1
        print(kl)
        kl.pop(0)
print(count)
