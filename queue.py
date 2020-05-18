class Node:
    def __init__(self, inputvalue):
        self.value = inputvalue
        self.next = None
        
# newnode = Node("David")

class Queue: #we can only add things to the back of the queue and remove them from the front
    def __init__(self):
        self.head = None 
        self.tail = None
        
    def enqueue(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self
    
    def dequeue(self):
        if self.head:
            frontVal = self.head
            self.head = self.head.next
            print('frontval',frontVal.value)
        else:
            print(None)
        return self
    
    def front(self):
        if self.head:
            print('front', self.head.value)
        else:
            print(None)
        return self
    
    def contains(self, val):
        runner = self.head
        print('runner.value',runner.value)
        while runner:
            if runner.value == val:
                return True
            else:
                runner = runner.next
        return False
    
    def isEmpty(self):
        if self.head:
            return True
        else:
            return False
    
    def size(self):
        runner = self.head
        count = 0
        while runner:
            count +=1
            runner = runner.next
        return count
    
    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
        
    #enqueue(val) -add val to Queue
    #dequeue(): remove and return front value
    #front(): return (not remove) first val
    #contains(val): Queue contains val?
    #isEmpty(): queue contains no value?
    #size(): return num of vals in Queue
    
# class SLL:
#     def __init__(self):
#         self.head = None

newQueue = Queue()
newQueue.enqueue(5).enqueue(2).enqueue(10).display().dequeue().front().display()
print('is empty',newQueue.isEmpty())
print('contains 4', newQueue.contains(4))
print('size', newQueue.size())
newQueue.enqueue(3).enqueue(1)
print('size',newQueue.size())
