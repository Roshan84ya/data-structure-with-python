s=input()
d=dict()
sd=0
k=0
l=0
for i in range(len(s)):
    #print(s[i],d ,s[i] not in d)
    if s[i] not in d:
        d[s[i]]=1
        sd+=1
    else:
        while s[i]  in d:
            #print(1)
            del d[s[l]]
            l+=1
            sd-=1
        d[s[i]]=1
        sd+=1
    k=max(k,sd)
print(k)
