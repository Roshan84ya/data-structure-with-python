"""You are given a string. Take the first character of the string and
put it at the end of the string.

Find out what the string will be after N steps.The string can be considered
as a queue. At each step, dequeue the character from the front and enqueue
it at the end. Repeat this process N times."""

from queue import Queue

q=Queue()
s="abcd"
N=3
for i in s:
    q.put(i)

print("Here is our queue from Front --> rear ")

for i in range(N):
    q.put(q.get())
while not q.empty():
    print(q.get(),end="")
