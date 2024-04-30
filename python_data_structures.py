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
            current_node, previous_node = current_node.next, current_node

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
        self.length += 1
        return True

    def insert(self, value, index):
        # Note that this method doesn't insert a node in the last position, use append for this usecase
        node_to_insert = Node(value)
        i = 1
        current_node = self.head.next
        prev_node = self.head

        while (i < self.length):
            if index >= self.length:
                raise IndexError("Index out of range")
            if index == 0:
                node_to_insert.next = self.head
                self.head = node_to_insert
                self.length += 1
                return True

            if i == index:
                prev_node.next = node_to_insert
                node_to_insert.next = current_node
                self.length += 1
                return True
            temp = current_node
            current_node = current_node.next
            prev_node = temp
            i += 1


# Sandbox
myLinkedList = LinkedList(1)

# Test append
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.append(5)
myLinkedList.append(6)

# Test insert
myLinkedList.insert(55, 5)

# Test delete

# myLinkedList.delete(1)
# Test pop
# print(myLinkedList.pop().value)

# Test print
myLinkedList.print_list()
# print(myLinkedList.length)
