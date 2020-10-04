def equal(s1,s2,n1):
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    i,j,count=0,0,0
    while i<n1 and j<n1:
        if s1[i]==s2[j]:
            count+=1
            i+=1
            j+=1
        elif s1[i]<s2[j]:
            i+=1
        elif s1[i]>s2[j]:
            j+=1

    return n1-count


        
 
def greater(s1,s2,n1):
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    i,j,count=0,0,0
    while i<n1 and j<n1:
        
        if s1[i]>s2[j]:
            count+=1
            i+=1
            j+=1
        elif s1[i]<=s2[j]:
            i+=1
    return n1-count
    
            
 
def smaller(s1,s2,n1):
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    i,j,count=0,0,0
    while i<n1 and j<n1:
        if s1[i]<s2[j]:
            count+=1
            i+=1
            j+=1
        elif s2[j]<=s1[i]:
            j+=1
    return n1-count
            
        
    
 
 
n=int(input())
s=input()
 
str1=s[:n//2]
str2=s[n//2:]
 
e=equal(str1,str2,n//2)
g=greater(str1,str2,n//2)
s=smaller(str1,str2,n//2)

print(min(e,g,s))
