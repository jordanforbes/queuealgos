def minToFront(someSLL):
    pass
    #search through SLL to find minimum and set that as the head.
    
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None 
    
    def add_to_front(self, val):
        if self.head == None:
            newnode = Node(val)
            self.head = newnode
        else:
            newnode = Node(val)
            newnode.next = self.head
            self.head = newnode
        return self 
    
    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next


newList = SLL()



newList.add_to_front(2).add_to_front(4).add_to_front(1).add_to_front(5)


def movemintoFront(sll):
    minim = sll.head
    runner = sll.head
    while runner.next != None:
        if runner.value < minim.value:
            minim = runner
        runner = runner.next 
    minim.next = sll.head
    
    return sll 


movemintoFront(newList)
# newList.display()
newList.display()
