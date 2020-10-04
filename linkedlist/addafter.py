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
            print("No element is present in the linkedlist")
            return
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.link

    def addafter(self,pos,data):
        count=1
        temp=self.head
        if pos==1:
            data=Node(data,self.head)
            self.head=data
            return
        
        while count<(pos-1) and temp:
            temp=temp.link
            count+=1
        if count==pos-1 and temp:
            data=Node(data,temp.link)
            temp.link=data
        else:
            print("There are less element")

ll=Linkedlist()
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.display()
print()
ll.addafter(9,2)
print()
ll.display()
