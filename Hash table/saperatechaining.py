#hashfunction= ord(i)*posititon(i) where i is the character in the string

k=19
dict1={i:[] for i in range(1,k+1)}

for i in range(4):
    s=input()
    sum1=sum([ord(s[j])*(j+1) for j in range(len(s))])
    dict1[sum1%19].append(s)

    
n=input("Enter the key you want to search:- ")

sum1=sum([ord(n[j])*(j+1) for j in range(len(n))])
    


if len(dict1[sum1%19]):
    flag=1
    for i in range(len(dict1[sum1%19])):
        if dict1[sum1%19][i]==n:
            print("Element found at {},{}".format(sum1%19,i+1))
            flag=0
    if flag:
        print("Not found")
                              
else:
    print("element not found")

