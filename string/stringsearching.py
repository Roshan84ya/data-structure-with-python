#searching a pattern in the given string

t='abcd'
p='xyz'
i=0
while i<((len(t)-len(p))+1):
    if t[i:i+len(p)]==p:
        print(i)
    i+=1
