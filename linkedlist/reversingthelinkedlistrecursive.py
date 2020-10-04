.;class Node:

    def __init__(self,data,link=None):
        self.data=data
        self.link=link

class Linkedlist:

    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.link!=None:
                temp=temp.link
            temp.link=Node(data)

    def display(self):
        if self.head==None:
            print("Linked list is empty")
            return
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.link

            
    def reversing(self,curr,prev):
        if curr.link is None:
            self.head=curr
            curr.link=prev
            return
        next=curr.link
        curr.link=prev
        self.reversing(next,curr)

    def reverse(self):
        if self.head is None:
            return
        self.reversing(self.head,None)

ll=Linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
print("The linked list is ")
ll.display()
ll.reverse()
print("\nThe reversed linked list is")
ll.display()
