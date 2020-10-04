class Node:

    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class Tree:
    diff=99999999
    ans=99999999
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=Tree.utilinsert(self.root,data)

    @staticmethod
    def utilinsert(root,data):
        if root is None:
            root=Node(data)
            
        elif data<root.data:
            root.left=Tree.utilinsert(root.left,data)
        else:
            root.right=Tree.utilinsert(root.right,data)
        return root # we are returning the updated varible root
    @staticmethod
    def inorder(root):
        if root is None:
            return
        Tree.inorder(root.left)
        print(root.data," ")
        Tree.inorder(root.right)
    @staticmethod
    def closest(root,d):
        if root is None:
            return
        Tree.closest(root.left,d)
        if abs(root.data-d)<Tree.diff:
            Tree.diff=abs(root.data-d)
            Tree.ans=root.data
        Tree.closest(root.right,d)

        return Tree.ans
        
        
            
t=Tree()
t.insert(10)
t.insert(5)
t.insert(2)
t.insert(5)
t.insert(1)
t.insert(15)
t.insert(13)
t.insert(22)
t.insert(14)
Tree.inorder(t.root)
print(Tree.closest(t.root,12))
            
