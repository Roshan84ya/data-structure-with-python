class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
from Node import Node
class LinkedList:
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
            print("Empty")
            return
        
        
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.link
                
import LinkedList as LL

ll = LL.LinkedList()
choice="Yes"
while choice=="Yes":
    data = int(input("Enter the value\n"))
    ll.append(data)
    choice = input("Do you want to add another node? Type Yes/No\n")

print("The elements in the linked list are ",end="")
ll.display()

