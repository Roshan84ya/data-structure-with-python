#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&limit=100&page=2&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
#important question and approch

#here we have certain popple in the line and they are giving each other bribe i.e
#one person can bribe another person that is ahead of him and can go to forward and one person can
"""# take bribe form the two people
#so the person who is standing at the last position can'not go more than two position ahead
"""so here we are taking the men from the behind and removing the
#men after we found it and by counting the bribe i.e if the person is at it's initial position then he havn't took any bribe but if if he had taken bribe one time then he must be moved
# one index ahead and if he had given broibe to the two people then he must given bribe to the two people so that's why we are checking from the behind that if person is not found in
#in range of 0<x<2 from behind the he must had given bribe to the more than two person"""
for _ in range(int(input())):
    input()
    q = [int(x) for x in input().split()]
    bribes = 0
    valid = True
    for i in reversed(range(len(q))):
        v = i + 1
        print(q,v)
        
        if q[-1] == v:
            q.pop(-1)
        elif len(q) > 1 and q[-2] == v:
            q.pop(-2)
            bribes += 1
        elif len(q) > 2 and q[-3] == v:
            q.pop(-3)
            bribes += 2
        else:
            valid = False
            break
        
    if valid:
        print(bribes)
    else:
        print("Too chaotic")
