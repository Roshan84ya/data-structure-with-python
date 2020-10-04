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
            print("The linked list is empty")
            return
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.link
    def middleelement(self):
        s=self.head
        f=self.head.link
        while f!=None:
            s=s.link
            f=f.link.link
        
        print(s.data)
        return

ll=Linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.display()
print("\nthe middle element is ")
ll.middleelement()

    
