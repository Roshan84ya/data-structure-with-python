class Node:

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
            print("empty linkedlist")
            return
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.link

    def appendmiddle(self,data):
        one=self.head
        fast=self.head.link
        while (fast and fast.link and fast.link.link):
            one=one.link
            fast=fast.link.link

        temp=one.link
        one.link=Node(data,temp)
            
ll=Linkedlist()
ll.append(1)
ll.append(2)
ll.append(1)
ll.append(2)
ll.append(1)
ll.append(2)
ll.append(1)
ll.append(2)
ll.append(1)
ll.append(1)
ll.display()
print()
ll.appendmiddle(20)
ll.display()

        
        
