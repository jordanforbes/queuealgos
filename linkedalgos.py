class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
class SLL:
    def __init__(self):
        self.head = None 
    
    def addfront(self, value):
        if self.head == None:
            newnode = Node(value)
            self.head = newnode
        else:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode
        return self 
    
    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
    
    def length(self):
        count = 0
        runner = self.head
        while runner != None:
            count +=1
            runner = runner.next
        print(count)
        return count 
    
    def addback(self, value):
        newnode = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = newnode
        return self
    
    
        
sll1 = SLL()
sll1.addfront(3).addback(4).addback(50)

def moveMaxToFront(sllinput):
    runner = sllinput.head
    maxval = runner.value
    while runner != None:
        if runner.next.value > maxval:
            maxval = runner.next.value
            maxnode = runner.next 
            before = runner 
            
        runner = runner.next 
    before.next = maxnode.next 
    maxnode.next = sllinput.head 
    sllinput.head = maxnode 
    
    return sllinput 

moveMaxToFront(sll1)
sll1.display()