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
            pass
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.link
    def addafter(self,pos,data):
        count=0
        
            
        temp=self.head
        while count<pos and temp.link:
            temp=temp.link
            count+=1
        if count==pos :
            data=Node(data,temp.link)
            temp.link=data
        else:
            print("There are less than {} elements in the linked list".format(pos))
        

import LinkedList as LL

ll = LL.LinkedList()
choice="Yes"
while choice=="Yes":
    data = int(input("Enter the value\n"))
    ll.append(data)
    choice = input("Do you want to append another node? Type Yes/No\n")

print("The elements in the linked list are ",end="")
ll.display()
choice1 =  "Yes"
while choice1 == "Yes":
    position = int(input("\nEnter the position after which you want to add another node"))
    data = int(input("\nEnter the value\n"))
    ll.addafter(position,data)
    print("The elements in the linked list are ",end="")
    ll.display()
    choice1 = input("\nDo you want to add another node after a certain position? Type Yes/No")
    
