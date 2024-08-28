class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        
    #push
    def push(self, item):
        self.items.append(item)
    #pop
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack") #error raise kar do 
    #peek
    def peek(self):
        if not self.is_empty():
            return self.items[-1] #last value of array 
        else:
            raise IndexError("peek from empty stack")
    #size 
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack)  # Output: Stack: [1, 2, 3]
    print("Pop:", stack.pop())  # Output: Pop: 3
    print("Peek:", stack.peek())  # Output: Peek: 2 ; stack = [1, 2]
    print("Stack size:", stack.size())  # Output: Stack size: 2 ; stack = [1, 2]
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False ; stack = [1, 2]
