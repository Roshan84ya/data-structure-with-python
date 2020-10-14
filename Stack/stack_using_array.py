class Stack:

    def __init__(self, limit: int):
        self.stack = []
        self.limit = limit

    def __str__(self) -> str:
        return *self.stack

    def push(self, data):
        """ 
        Push an element to the top of the stack.
        """
        if len(self.stack) >= self.limit:
            raise Exception('Stack is full!')
        self.stack.append(data)

    def pop(self) -> data:
        """ 
        Removes an element from the top of the stack.
        """
        return self.stack.pop()

    def peek(self) -> data:
        """
        Peek at the top-most element of the stack.
        """
        return self.stack[-1]

    def isEmpty(self) -> bool:
        """
        Returns true if stack is empty.
        """
        return True if not self.size() else False

    def isFull(self) -> bool:
        """
        Returns true if stack is full.
        """
        return self.size() == self.limit

    def size(self) -> int:
        """
        Returns the size of the stack.
        """
        return len(self.stack)

    def isAvailable(self, item) -> bool:
        """
        Returns true if item is in stack.
        """
        return item in self.stack
