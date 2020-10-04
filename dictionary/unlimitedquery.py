import sys
from collections import defaultdict
k=defaultdict(list)
n=int(input())
while True:
    query=sys.stdin.readline().strip()
    a,b=query.split()
    print(a,b)
    if query=="":
        break
