import unittest
from MultiStack import MultiStack

class MultiStackTest(unittest.TestCase):
    stack1 = 0
    stack2 = 1
    stack3 = 2

    def test_new(self):
        #Arrange
        total = 3
        size = 9
        index1 = -1
        index2 = 2
        index3 = 5
        #Act
        target = MultiStack(total)
        #Assert
        self.assertEqual(target.total, total)
        self.assertEqual(size, len(target.store))
        self.assertEqual(index1, target.index1)
        self.assertEqual(index2, target.index2)
        self.assertEqual(index3, target.index3)

    def test_push(self):
        #Arrange
        total = 3
        index1 = 0
        index2 = 3
        index3 = 6
        item1 = 23
        item2 = 42
        item3 = 73
        #Act
        target = MultiStack(total)
        target.push(self.stack1, item1)
        target.push(self.stack2, item2)
        target.push(self.stack3, item3)
        #Assert
        self.assertEqual(index1, target.index1)
        self.assertEqual(index2, target.index2)
        self.assertEqual(index3, target.index3)
        self.assertEqual(item1, target.store[index1])
        self.assertEqual(item2, target.store[index2])
        self.assertEqual(item3, target.store[index3])

    def test_peek(self):
        #Arrange
        total = 3
        index1 = 0
        index2 = 3
        index3 = 6
        item1 = 23
        item2 = 42
        item3 = 73
        #Act
        target = MultiStack(total)
        target.push(self.stack1, item1)
        target.push(self.stack2, item2)
        target.push(self.stack3, item3)
        #Assert
        self.assertEqual(item1, target.peek(self.stack1))
        self.assertEqual(item2, target.peek(self.stack2))
        self.assertEqual(item3, target.peek(self.stack3))
        self.assertEqual(index1, target.index1)
        self.assertEqual(index2, target.index2)
        self.assertEqual(index3, target.index3)

    def test_pop(self):
        #Arrange
        total = 3
        index1 = -1
        index2 = 2
        index3 = 5
        item1 = 23
        item2 = 42
        item3 = 73
        #Act
        target = MultiStack(total)
        target.push(self.stack1, item1)
        target.push(self.stack2, item2)
        target.push(self.stack3, item3)
        #Assert
        self.assertEqual(item1, target.pop(self.stack1))
        self.assertEqual(item2, target.pop(self.stack2))
        self.assertEqual(item3, target.pop(self.stack3))
        self.assertEqual(index1, target.index1)
        self.assertEqual(index2, target.index2)
        self.assertEqual(index3, target.index3)