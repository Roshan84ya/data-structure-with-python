a=input()
b=input()
if len(a)<len(b):
    a="0"*(len(b) -len(a) )+a
elif len(b)<len(a):
    b="0"*(len(a) - len(b))+b
        
ans=""
carry=0
print(a,b)
for (i,j) in zip(a[::-1],b[::-1]):
    if i!=j :
        if carry==0:
            ans+="1"
            carry=0
        else:
            ans+="0"
            carry=1
    elif i==j=="0":
        if carry==0:
            ans+="0"
        else:
            ans+="1"
            carry=0
    elif i==j=="1":
        if carry==0:
            ans+="0"
            carry=1
        else:
            ans+="1"
            carry=1
if carry==1:
    ans+="1"
print(ans[::-1])
