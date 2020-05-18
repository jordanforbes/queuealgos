class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None



class SLL:
    def __init__(self):
        self.head = None

    def removefront(self):
        if self.head == None:
            return self
        else:
            self.head = self.head.next
            return self

    def addtoFront(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        return self

    def contains(self, valueToFind):
        if self.head == None:
            return False
        else:
            runner = self.head
            while runner != None:
                if runner.value == valueToFind:
                    print("true")
                    return True
                else:
                    runner = runner.next
            print("false")
            return False
    def length(self):
        runner = self.head
        counter = 1
        # print(runner.next.next.next.next)
        while runner.next is not None:
            runner = runner.next
            counter +=1
            # print(counter)
        print(f'The Length is {counter}')
        return counter
    def display(self):
        ans = ''
        runner = self.head
        while runner.next is not None:
            ans = ans+ str(runner.value)+' '
            runner = runner.next
        ans = ans+ str(runner.value)+' '
        print(ans)
        return ans
        


def length(pointer):
    
    runner = pointer.head
    counter = 1
    # print(runner.next.next.next.next)
    while runner.next is not None:
        runner = runner.next
        counter +=1
        print(counter)
    return counter
    
def display(pointer):
    pass

a = Node(7)
b = Node(3)
c = Node(10)
d = Node(9)
a.next = b
b.next = c
c.next = d

newList = SLL()
newList.head = a

newList.length()
newList.display()
