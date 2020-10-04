def pallin(s):
    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

def solve(s):
    arr=list(s)
    if len(s)>1:
        i=0
        j=len(s)-1

        while j!=0:
            if s[i]!=s[j]:
                j-=1
            elif s[i]==s[j] and pallin(s[i:j+1]):
                break
            else:
                j-=1
        index=j+1
                
                
        
    else:
        return s
    while True:
        if pallin(s):
            return s
        else:
            s=arr[index]+s
            index+=1
            
            
                



s=input()
print(solve(s))

