class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            lastnode=self.head
            while lastnode.link!=None:
                lastnode=lastnode.link
            lastnode.link=Node(data)
    def display(self):
        if self.head==None:
            print("The linked list is empty")
            return
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" -> ")
                temp=temp.link
    def counting(self):
        count=0
        if self.head==None:
            return "The linked has {} element".format(count)
        else:
            temp=self.head
            while temp:
                count+=1
                temp=temp.link
            return "The linked has {} elements".format(count)
    
    
ll=linkedlist()
while input("Want to enter something in the linked list\n yes/no\n")=='yes':
    k=int(input("Enter the element you wanted to insert\n"))
    ll.append(k)
print("Your linked list is here")
ll.display()

print(ll.counting())
    
    
    
