class MultiStack:
    stacks = 3
    stack1 = 0
    stack2 = 1
    stack3 = 2

    def __init__(self, total):
         assert(total > 0), "Cannot initialize a stack with zero slots"
         self.total = total
         self.store = [0] * (self.total * self.stacks)
         self.index1 = (self.total * self.stack1) - 1
         self.index2 = (self.total * self.stack2) - 1
         self.index3 = (self.total * self.stack3) - 1

    def push(self, stack, item):
        assert(isinstance(stack, int)), "Stack number not valid"
        assert(stack >= self.stack1 and stack <= self.stack3), "Stack number not valid"
        # Los valores de "index" se deben almacenar en un arreglo
        if stack == self.stack1:
            self.index1 += 1
            self.store[self.index1] = item
        elif stack == self.stack2:
            self.index2 += 1
            self.store[self.index2] = item
        else:
            self.index3 += 1
            self.store[self.index3] = item
    
    def peek(self, stack):
        assert(stack >= self.stack1 and stack <= self.stack3), "Stack number not valid"
        if stack == self.stack1:
            result = self.store[self.index1]
        elif stack == self.stack2:
            result = self.store[self.index2]
        else:
            result = self.store[self.index3]
        return result

    def pop(self, stack):
        assert(stack >= self.stack1 and stack <= self.stack3), "Stack number not valid"
        result = self.peek(stack)
        if stack == self.stack1:
            self.index1 -= 1
        elif stack == self.stack2:
            self.index2 -= 1
        else:
            self.index3 -= 1
        return result
