class MinStack:

    def __init__(self):
        self.stack = [] #we know were going to have two stacks, lets define them now, implementing this with an array
        self.minStack = [] #initially empty

    def push(self, val: int) -> None:
        self.stack.append(val) #take the input value and append it to the first stack
        #for the minStack, we need to know if there is already a value inserted in the minStack, then we're going to take the min of the input value (val) and the value at the top of our minStack and take the minimum of those two and append it to the min Stack
        val = min(val, self.minStack[-1] if self.minStack else val) # min of itslef(min(val)) and the mimum of the top of our min stack, self.minStack[-1], but we know the min stack could be non empty so if we only do this if its non empty , if self.minStack, otherwise just take the min of val and val. We're taking the min of val and the top of our stack self.minStack[-1] if the stack is non empty, self.minStack, if it is empty we take the minimum of first val and second val
        self.minStack.append(val) # because if the stack is empty we just take the minStack and append the value of to it, val, so when we appned val ,it should be the minimum of the input val and mimimum of the top of the minStack, self.minStack[-1]
       
    def pop(self) -> None:
        self.stack.pop() # pop from both stacks, we dont have to return anything
        self.minStack.pop() # pop from both stacks, we dont have to return anything
        

    def top(self) -> int:
        return self.stack[-1] # to get the top value , we take from the top of the first stack, by top we want to get the last value that was inserted, self.stack[-1], it is always gonna be called when our stack is non empty we dont have to take care of any edge cases

    def getMin(self) -> int:
        return self.minStack[-1]#return from the top of the min stack , we're always returing minimum value which is going to always be at the top of the min stack, and its only going to b ecalled when our stack is non empty


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()