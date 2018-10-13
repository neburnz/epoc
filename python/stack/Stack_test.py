import unittest
from Stack import Stack

class StackTest(unittest.TestCase):

    def test_new(self):
        #Arrange
        index = -1
        total = 5
        #Act
        target = Stack(total)
        #Assert
        self.assertEqual(index, target.indice)
        self.assertEqual(total, len(target.arreglo))
    
    def test_push(self):
        #Arrange
        total = 3
        item = 1
        index = 0
        #Act
        target = Stack(total)
        target.push(item)
        #Assert
        self.assertEqual(index, target.indice)
        self.assertEqual(item, target.arreglo[index])
    
    def test_peek(self):
        #Arrange
        total = 3
        item = 2
        #Act
        target = Stack(total)
        target.push(item)
        #Assert
        self.assertEqual(item, target.peek())
    
    def test_pop(self):
        #Arrange
        index = -1
        total = 3
        item = 21
        #Act
        target = Stack(total)
        target.push(item)
        #Assert
        self.assertEqual(item, target.pop())
        self.assertEqual(index, target.indice)
