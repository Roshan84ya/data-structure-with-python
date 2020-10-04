class Node:

    def __init__(self,data,link=None):  #here we add data to data and initialize
                                        #link to null
        self.data=data
        self.link=link

class Linkedlist:

    def __init__(self):
        self.head=None
#here if we found the head is null i.e we don't have any element at the first position so then we make a node an add it to the head i.e head-->Node
#else if we have elements then we iterate till the last element and the we add ht element at the end

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
            while temp.link!=None:
                print(temp.data,'->',end=" ")
                temp=temp.link
            print(temp.data)


    def reversing(self):
        prev=None
        curr=self.head
        next=None
        while curr!=None:
            next=curr.link
            curr.link=prev
            prev=curr
            curr=next
        self.head=prev

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
ll.reversing()
print("\nThe reversed linked list is ")
ll.display()

