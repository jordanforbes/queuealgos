# class Node:


#     def __init__(self, value):
#         self.value = value
#         self.next = None



# # print('A: ', a.value)#head of list
# # print('B: ', b.value)
# # print('C: ', c.value)

# # print(a.value)
# # print(a.next.value) #a.next is the same as saying b
# # print(a.next.next.value)#should be the value of c

# #a list is a series of nodes

# class SLL:
#     def __init__(self):
#         self.head = None
#     def add_to_front(self, val):
#         pass
#     def remove_from_front(self):
#         pass

# a = Node(7)
# b = Node(3)
# c = Node(1)
# a.next = b
# b.next = c

# my_list = SLL()
# my_list.head = a

# print(my_list.head.value)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        # self.next = None
    def add_to_front(self, val):
        self.head = val
        
    def remove_from_front(self):
        pass
    
    def addback(self, value):
        newnode = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = None
        retuern self
        
a = Node(7)
b = Node(3)
c = Node(1)
d = Node(6)
a.next = b
b.next = c
c.next = d

my_list = SLL()

my_list.head = a

runner = my_list.head

counter = 1
while runner.next is not None:
    runner = runner.next
    counter += 1

# print(counter)

def addToList(list,val):
    list.add_to_front(Node(val))


class List:
    def contains(self, valueFind):
        if self.head == None:
            return False
        else:
            runner = self.head
            while runner !=None;
                if runner.value == valueFind:
                    print('True')
                    return True
                else:
                    runner = runner.next
                print('False')
                return False



addToList(my_list,'Rudy')

print(my_list.head.value)

counter = 1


addToList(my_list,'Tad')
print(my_list.head.value)

    
value = 1
counter = 1
while runner.next is not None:
    if(runner.value == value):
        print('Found')
    runner = runner.next
    counter +=1
