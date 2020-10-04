class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
        
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

obj=LinkedList()
while True:
    k=int(input("Enter the vlaue\n"))
    
    obj.append(k)
    if input("Do you want to add another node? Type Yes/No \n")=="No":
        
        break
print("The element of the Linked list is ",end=" ")
obj.display()
        
        
