import sys
n = int(input())
phoneBook = {}
for n in range(n):
    entry = input()
    name, phoneNumber = entry.split(' ')
    if len(phoneNumber)>8:
        phoneBook = phoneNumber[:8]
    phoneBook.update({name: phoneNumber})
while True:
    query = sys.stdin.readline().strip()
    if query=='':
        break
    output = phoneBook.get(query)
    
   
    print(f'{query}={output}') if output else print('Not found')
