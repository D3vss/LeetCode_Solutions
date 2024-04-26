# Linked Lists
"""
- What are LinkedLists? 
  Instead of having all the elements of a list be ordered in memory, //
  a linked list resembles a normal list in essence (in being a linear //
  collection of data), all of the elements of a linked list are scattered //
  in random postions in memory and every element points to the next element.

- Creation logic
  A linked list is not a primitive type in python unlike a list. That's why //
  we need to create a class for it. In a linkedin list, we should be able to append,//
  prepend, and insert at any given index. As well as delete any given node.
  In total we will need to create 5 methods: a constructor, append, prepend, insert, and delete.
  The 1st four methods will always create a Node (a container for our data and the pointer for the next element). 
  The best practice is to create a separate class for node creation that we will refer to it in //
  each method instead of duplicating boilerplate.
"""


class Node:
    def __init__(self, value):
        self.value = value
        # for now our Node has no next, but this value will be overrided during Node creation.
        self.next = None


class LinkedList:

    def __init__(self, value):
        # create the first node in the list
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1

    def print_list(self):
        current_node = self.head
        # None is a none truthfull expression, so it is equivalent to False.
        while (current_node.next):
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)

    def append(self, value):
        # Verify if the list is empty or not, cuz logic varies.
        tail = self.tail
        node_to_append = Node(value)

        if self.length == 0:
            self.head = self.tail = node_to_append
        else:
            tail.next = self.tail = node_to_append
        self.length += 1
        return True

    def pop(self):
        tail = self.tail
        current_node = self.head
        previous_node = None
        while (current_node != tail):
            current_node = current_node.next
            previous_node = current_node

        tail = previous_node
        previous_node.next = None
        return current_node

    def prepend(self, value):
        node_to_prepend = Node(value)
        head = self.head
        if self.length == 0:
            self.head = self.tail = node_to_prepend
        else:
            node_to_prepend.next = head
            head = node_to_prepend
    # def insert(self, index, value):
    # def delete(self, index):


# Sandbox

myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)

# myLinkedList.print_list()

print(myLinkedList.pop().value)
