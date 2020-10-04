"""
LInked list every kind of operations in the linked list

"""                                                #making a linked list and adding element to it at the end

                                                #here we made a node class 
class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link
        
###################################################################################################################################################

        
class Linkedlist:
  ############################                  #here we initialized the start element with the null ie start-->null
    def __init__(self):
        self.head=None

        
   ############################                 #to addthe element at the end of the linked list
    def addelement(self,data):
        
                                                #firstly we'll check if the first poition is empty the we add it there
                                                #else the we traverse till the last an dthen we append that element at the last
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head                      #ex 1-->2-->3--Null we take temp-->1 if 1.link!=none the we do it till we got temp.link==None and hence loop will be broke and the we will go to the temp.link
                                                #and assign that Node(data)
            while temp.link:
                temp=temp.link
            temp.link=Node(data)
        


   ###########################                  #To display the element
    def display(self):
                                                #firstly we will check if the first element is null then it we dont have any element in the linked list so we are not going to print anything
        if self.head==None:
            print("No element is present")
            return
        else:
            print("The element are:-")                                  #here we store the value of ponting varible to the fisrt node to an temp
            temp=self.head
                                                #and here we are checking whether the temp.link!=NOne so that then we'll able to print the data of it
            while temp.link:
                print(temp.data,end=" --> ")
                temp=temp.link
            print(temp.data)

                                                #here we are adding the element at that position
 ###################################
    def addafterposition(self,pos,data):
                                                #position should be start from 1 or positive integer
        if pos<1:
            print("enter only positive integer")
            return
        
        count=1
        temp=self.head
                                                #if we want to add the element at the first position the the we can point our start at to that data and at the linke field of that data we need to put the link of the start
        if pos==1:
            self.head=Node(data,self.head)
            Linkedlist.display(self)
            return
                                            #'''else we are going to stop 1 position before i.e if the position is 2 then we are going to stop at position 1 anc at the link of 1 
                                               # we are going to put that Node, and in the link field of that node we are going to put 1.link  as as the link field
                                                #of 1 is now become the link field of that new node(data,and 1.link) it is applied for the all even for the last node'''
        
        while count<pos-1 and temp:
            temp=temp.link
            count+=1
        if (pos-1)==count and temp:
            temp.link=Node(data,temp.link)
            Linkedlist.display(self)
        else:
            print("less element")

#########################################
    #adding at the first place 
    def addatfirst(self,data):
        self.head=Node(data,self.head)
        Linkedlist.display(self)


#########################################
    #adding at the middle
    def addatmiddle(self,data):
        if self.head==None:
            print("No element present")
            return
        slow=self.head
        fast=self.head
        while fast.link and fast.link.link and fast.link.link:
            slow=slow.link
            fast=fast.link.link
        slow.link=Node(data,slow.link)
        Linkedlist.display(self)
#########################################################
    #remove form the first position
        
    def remf(self):
        temp=self.head
        self.head=self.head.link
        del temp
        Linkedlist.display(self)

########################################################
    #remove from the last node
    def reml(self):
        temp=self.head
        while temp.link and temp.link.link:
            temp=temp.link
        f=temp.link
        
        temp.link=None
        del f
        Linkedlist.display(self)
######################################################
    #remove from the position p
    def remp(self,pos):
        if pos==1:
            Linkedlist.remf(self)
        else:
            temp=self.head
            count=1
            while count<(pos-1) and temp.link:
                count+=1
                temp=temp.link
            if count<(pos-1) and temp.link:
                temp.link=temp.link.link
                Linkedlist.display(self)
            else:
                print("less number of element")
            
            
        

#############################################################################################################################

#creating object of Linkedlist
ll=Linkedlist()
ll.addelement(1)
ll.addelement(2)
ll.addelement(3)
ll.addelement(4)
print("Initially",end=" ")
ll.display()

#addelement means adding at the end
while True:
    print("\n**********************  Options *******************************\n")
    print("To add element Type:-1")
    print("To display Type:- 2")
    print("To delete an element Type :- 3")
    print("To quiet Type :- 4")
    
    k=input()
    if k=="1":
        element=int(input("Enter the element you wanted to add:- "))
        print("To add element Type:- 1")
        print("To add at first Type:- 2")
        print("To add at last Type:- 3")
        print("To add at middle Type:-4")
        print("To add at Position Type:-5")
        sk=input()


        
        if sk=="1" or sk=="3":
            
            ll.addelement(element)

            
        elif sk=="2":
            ll.addatfirst(element)
            
        elif sk=="4":
            ll.addatmiddle(element)
        elif sk=="5":
            position=int(input("Enter the position:- "))
            ll.addafterposition(position,element)
        
    elif k=="2":
        
        ll.display()
    elif k=="3":
        print("To delete from the front Type:- 1")
        print("To delete from the end Type:- 2")
        print("To delete from the random position Type:- 3")
        jkl=input()
        if jkl=="1":
            ll.remf()
        elif jkl=="2":
            ll.reml()
        elif jkl=="3":
            ij=int(input("Enter the position:- "))
            ll.remp(ij)
    
    elif k=="4":
        break




            
            
            


        
                
        

    

