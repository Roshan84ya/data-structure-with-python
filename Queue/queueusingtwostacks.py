from queue import LifoQueue

stack1=LifoQueue()
stack2=LifoQueue()


for i in range(int(input())):
    k=input().split()
    
    if k[0]=="1":
        
        stack1.put(int(k[1]))
        
    elif k[0]=="2":
        if stack2.empty()!=True:
            stack2.get()
            
            
        else:
            while stack1.empty()!=True:
                stack2.put(stack1.get())
            kf=stack2.get()
            
        
        
    
    elif k[0]=="3":
        if stack2.empty()!=True:
            kf=stack2.get()
            print(kf)
            stack2.put(kf)
        else:
            while stack1.empty()!=True:
                stack2.put(stack1.get())
            kf=stack2.get()
            print(kf)
            stack2.put(kf)
            
