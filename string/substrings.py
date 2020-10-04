#recursive
"""def allp(s,sub,i,n,kl):
    if sub!="":
        kl.add(sub)
    if i<n:
        
        
        allp(s,sub,i+1,n,kl) or allp(s,sub+s[i],i+1,n,kl)
    
    

s="abc"

kl=set()
allp(s,"",0,3,kl)
print(kl)
kl=list(kl)
kl.sort()
print(kl)"""
s="abc"
s=input()
n=len(s)
kl=[]
for i in  range(1,2**len(s)):
    k=bin(i).replace("0b","")
    k=k[::-1]
    ans=""
    
    for j in range(len(k)):
        if k[j]=="1":
            ans+=s[j]
    kl.append(ans)
kl.sort()
print(kl)
        
        



