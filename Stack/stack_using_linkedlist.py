class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:

    def __init__(self):
        self.head = None
    
    def __str__(self) -> str:
        string = ''
        temp = self.head
        while temp is not None:
            string = string + temp.data + "->"
            temp = temp.next
        return string

    def push(self, data):
        """ 
        Push an element to the top of the stack.
        """
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    def pop(self) -> data:
        """ 
        Removes an element from the top of the stack.
        """
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def peek(self) -> data:
        """
        Peek at the top-most element of the stack.
        """
        return self.head.data

    def isEmpty(self) -> bool:
        """
        Returns true if stack is empty.
        """
        return self.head is None

    def size(self) -> int:
        """
        Returns the size of the stack.
        """
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def isAvailable(self, item) -> bool:
        """
        Returns true if item is in stack.
        """
        temp = self.head
        while temp is not None:
            if temp.data == item:
                return True
            temp = temp.next
        return False
