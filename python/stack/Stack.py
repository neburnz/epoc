class Stack:
    def __init__(self, total):
        assert(total > 0), "Cannot initialize a stack with zero slots"
        self.total = total
        self.arreglo = [0] * self.total
        self.indice = -1

    def push(self, item):
        assert(self.indice < self.total), "The stack is full"
        self.indice += 1
        self.arreglo[self.indice] = item

    def peek(self):
        assert(self.indice > -1 and self.indice < self.total), "Index out of range"
        resultado = self.arreglo[self.indice]
        return resultado

    def pop(self):
        assert(self.indice > -1), "The stack is empty"
        resultado = self.peek()
        self.indice -= 1
        return resultado