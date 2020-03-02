# Joe Degere
# 3/3/2020
# Double Linked List Practice


class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

# This function adds to the beginning of the linked list

    def add_head(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node

# This function adds to the end of the linked list

    def add_end(self, data):
        new_node = Node(data=data)
        curr = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

# This function removes from the head of the linked list

    def remove_head(self):
        if self.head is None:
            return None
        else:
            self.head = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return self.head

# This function removes from the end of the linked list

    def remove_end(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None
        return curr.data
