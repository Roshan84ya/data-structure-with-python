#counting frequency in the string

def countnostring(s):
    a=[0]*26
    for i in s:
        a[ord(i)-97]+=1
    for i in range(len(a)):
        if a[i]!=0:
            print(chr(97+i),a[i])



s=input()
countnostring(s)
