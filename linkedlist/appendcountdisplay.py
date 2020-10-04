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
            print("Empty linked list")
            return
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.link

    def count1(self):
        if self.head==None:
            return 0
        else:
            temp=self.head
            count=1
            while temp.link!=None:
                temp=temp.link
                count+=1
        return count

ll=Linkedlist()
c="Yes"

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.display()
"""while c=="Yes":
    k=int(input("Enter the value\n"))
    ll.append(k)
    c=input("Do you want to add another node? Type Yes/No\n")
print("The element in the linkedlist ",end=" ")
ll.display()
print()
print("The number of the element in the linked list {}".format(ll.count1()))
ll.count1()"""
