strarr=input().split(",")
queries=input().split(",")

presum=[0]*(len(strarr)+1)
sum1=0
for i in range(len(strarr)):
    if strarr[i][0] in "aeiou" and strarr[i][-1] in "aeiou":
        sum1+=1
    presum[i+1]=sum1
for i in queries:
    s,e=map(int,i.split("-"))
    print(presum[e]-presum[s-1])
    
    
    
    
    
