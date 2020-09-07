'''
    This module provides linked list class with yet insert and remove_first methods.
'''

from ctypes import Structure, c_int, POINTER, pointer

class Node(Structure):
    ''' The class represents linked list node with C-like efficiency. '''

Node._fields_ = [("data", c_int),
                 ("next", POINTER(Node))]

class LinkedList():
    ''' The class represents linked list. '''
    __slots__ = ("__head")

    def __init__(self, data=None):
        ''' Self initialization. '''
        self.__head = pointer(Node(data = c_int(data)))

    def __str__(self):
        ''' Print linked list on string representation. '''
        if self.__head is None:
            return "The linked list is empty."

        linked_list_str = ""

        current_node = self.__head

        while current_node.contents.next:
            linked_list_str += str(current_node.contents.data) + " -> "
            current_node = current_node.contents.next

        linked_list_str += str(current_node.contents.data)

        return linked_list_str

    def __repr__(self):
        ''' Print linked list on string representation. '''
        if self.__head is None:
            return "The list is empty."

        linked_list_str = ""

        current_node = self.__head

        while current_node.contents.next:
            linked_list_str += str(current_node.contents.data) + " -> "
            current_node = current_node.contents.next

        linked_list_str += str(current_node.contents.data)

        return linked_list_str

    def insert(self, data):
        ''' Inserts node with data argument in linked list head. ''' 
        new_node = Node(data = c_int(data))

        new_node.next = self.__head

        self.__head = pointer(new_node)

    def remove_first(self):
        ''' Removes linked list first node and set head on the next node. '''
        self.__head = self.__head.contents.next

if __name__ == '__main__':
    linked_list = LinkedList(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print(linked_list)

    linked_list.remove_first()
    print(linked_list)
