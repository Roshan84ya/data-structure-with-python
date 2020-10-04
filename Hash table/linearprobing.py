k=19
dict1={i:[] for i in range(1,k+1)}
for i in range(4):
    s=input()
    sum1=0
    for j in range(len(s)):
        sum1+=ord(s[i])
    dict1[sum1%19].append(s)
for i in dict1:
    if len(dict1[i])!=0:
        print(i,dict1[i])
        
n=input("Enter the key you want to search:- ")
sum1=sum([(i+1)*ord(n[i]) for i in range(len(n))])
if len(dict1[sum1%19]):
    print(sum1%19)
else:
    print("element not found")
