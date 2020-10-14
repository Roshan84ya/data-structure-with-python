class Node:

    def __init__(self,data: int,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.data


class BinarySearchTree:
    
    diff=float('inf')
    ans=float('inf')

    def __init__(self):
        self.root=None

    def insert(self,data: int) -> int:
        '''
        Inserts the data in tree using iteration.
        '''

        # using Recursion 
        # Recursion is usually heavier than Intarion in terms of space 
        # as each recursive call allocates new space on the stack.

        # if self.isEmpty():
        #     self.root = Node(data)
        # elif data < self.root.data:
        #     self.root.left = self.insert(data)
        # else:
        #     self.root.right= self.insert(data)

        #using Iteration
        if self.isEmpty():
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                elif data >= current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
    
    def preOrder(self) -> list:
        '''
        Returns a list with values in Pre-Order(Node, Left, Right)
        '''
        if self.isEmpty():
            return []
        values = list()
        values = [self.root.data] + self.preOrder(self.root.left) + self.preOrder(self.root.right)
        return values
        
    def inOrder(self) -> list:
        '''
        Returns a list with values in PostOrder(Left, Node, Right)
        '''
        if self.isEmpty():
            return []
        values = list()
        values = self.inOrder(self.root.left) + [self.root.data] + self.inOrder(self.root.right)
        return values
    
    def postOrder(self) -> list:
        '''
        Returns a list with values in PostOrder(Left, Right, Node)
        '''
        if self.isEmpty():
            return []
        values = list()
        values = self.postOrder(self.root.left) + self.postOrder(self.root.right) + [self.root.data]
        return values

    def levelOrder(self) -> list:
        '''
        Returns a list with values in Level Order Traversal.
        '''
        if self.isEmpty():
            return []
        values = list()
        queue = [self.root]
        while(len(queue)>0):
            node = queue.pop(0)
            values.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return values
    
    def isEmpty(self) -> bool:
        '''
        Returns true if tree is empty else false.
        '''
        return self.root is None
    
    def search(self, value: int) -> Node:
        '''
        Returns the node if desired data is available.
        '''
        if self.isEmpty():
            return 'Tree is Empty!'
        else:
            node = self.root
            while node is not None:
                node = node.left if value < node.data else node.right
            return node
    
    def max_value(self, node=None) -> int:
        """
        Returns the biggest item from the Tree.
        """
        if node is None:
            node = self.root
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node.data

    def min_value(self, node=None) -> int:
        """
        Returns the smallest item from the Tree.
        """
        if node is None:
            node = self.root
        if not self.empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node.data
    
    def isFull(self) -> bool:
        """
        Returns true if tree is full.
        """
        if not self.root:
            return True
        if self.root.left and self.root.right:
            return isFull(self.root.left) and isFull(self.root.right)
        else:
            return not self.root.left and not self.root.right
    
    def depth(self) -> int:
        '''
        Return Depth/Height of Tree.
        '''
        return 1 + max(depth(self.root.left), depth(self.root.right)) if self.root else 0
