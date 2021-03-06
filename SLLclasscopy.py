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
sll1.addfront(5).addfront(6).addfront(8).addfront(12).addback(23).display()

def movemintoFront(sllinput):
    # yoursolutionhere
    return sllinput


movemintoFront(sll1)
