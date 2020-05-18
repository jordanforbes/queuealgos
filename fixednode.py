class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def addfront(self, value):
        #some solution here that adds a node to the singly linked list

        if self.head == None:
            newnode = Node(value)
            self.head = newnode
        else:
            newnode = Node(value)
            newnode.next= self.head
            self.head = newnode
        return self

    def display(self):
        #some solution here that prints each value from the nodes in the list to the terminal
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

    def removeback(self):
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        runner.next = None
        return self


sll1 = SLL()
sll1.addfront(5).addback(6).addback(8).addback(-23).addback(12).addback(3)

def movemintoFront(sllinput):
    runner = sllinput.head
    minval = runner.value
    while runner != None:
        if runner.next != None:
            if runner.next.value < minval:
                minval = runner.next.value
                minnode = runner.next
                before = runner

        runner = runner.next
    before.next = minnode.next
    minnode.next = sllinput.head
    sllinput.head = minnode


    return sllinput


# movemintoFront(sll1)
# sll1.display()
sll1.display()
print('execution')

def moveMaxToFront(sllinput):
    runner = sllinput.head
    maxval = runner.value
    while runner != None:
        if runner.next != None:
            if runner.next.value > maxval:
                maxval = runner.next.value
                maxnode = runner.next 
                before = runner 
            
        runner = runner.next 
    before.next = maxnode.next 
    maxnode.next = sllinput.head 
    sllinput.head = maxnode 
    
    return sllinput 

def moveMaxToBack(sllinput):
    runner = sllinput.head
    maxval = runner.value
    maxnode = runner 
    while runner.next != None:
        if runner.next.value > maxval:
            maxval = runner.next.value
            maxnode =runner.next 
            before = runner 
        runner = runner.next 
    if sllinput.head.value != maxval:
        before.next = maxnode.next 
        runner.next = maxnode
        maxnode.next = None 
    else:
        runner.next =maxnode 
        sllinput.head = sllinput.head.next 
        maxnode.next = None 
            
    return sllinput 

moveMaxToFront(sll1)
sll1.display()