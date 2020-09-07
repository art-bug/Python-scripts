'''
    This module provides double linked list class with
    insert and remove methods and iterating ability.
'''

class DoubleNode:
    ''' The class represents double linked list node. '''
    __slots__ = ("data", "next", "prev")

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    ''' The class represents double linked list. '''
    __slots__ = ("__head", "__tail", "__current_node")

    def __init__(self, data=None):
        ''' Self initialization. '''
        self.__head = DoubleNode(data)
        self.__tail = self.__head
        self.__current_node = self.__head

    def __iter__(self):
        ''' Returns iterator of the double linked list. '''
        self.__current_node = self.__head
        return self

    def __next__(self):
        ''' Returns a data of the next node in the double linked list. '''
        if not self.__current_node:
            raise StopIteration

        data = self.__current_node.data

        self.__current_node = self.__current_node.next

        return data

    def prev(self):
        ''' Returns a data of the previous node in the double linked list. '''
        self.__current_node = self.__current_node.prev

        if not self.__current_node:
            raise StopIteration

        data = self.__current_node.data

        return data

    def __str__(self):
        ''' Prints the double linked list in string representation. '''
        if not (self.__head and self.__tail):
            return "The double linked list is empty."

        double_linked_list_str = ""
        current_node = self.__head

        while current_node.next:
            double_linked_list_str += str(current_node.data) + " <-> "
            current_node = current_node.next

        double_linked_list_str += str(current_node.data)

        return double_linked_list_str

    def insert(self, data):
        ''' Inserts a node with data in the begin of the double linked list. '''
        new_node = DoubleNode(data)

        new_node.next = self.__head

        self.__head.prev = new_node

        self.__head = self.__head.prev

    def append(self, data):
        ''' Appends a node with data in the end of the double linked list. '''
        new_node = DoubleNode(data)

        new_node.prev = self.__tail

        self.__tail.next = new_node

        self.__tail = self.__tail.next

    def remove_first(self):
        ''' Removes the first node of the double linked list. '''
        if self.__head:
            if self.__head.next:
                self.__head = self.__head.next
                self.__head.prev = None
            else:
                self.__head = None

    def remove_last(self):
        ''' Removes the last node of the double linked list. '''
        if self.__tail:
            if self.__tail.prev:
                self.__tail = self.__tail.prev
                self.__tail.next = None
            else:
                self.__tail = None

    def __del__(self):
        ''' Destructs the double linked list. '''
        node_to_delete = None

        while self.__head:
            node_to_delete = self.__head
            del node_to_delete
            self.__head = self.__head.next

def __demonstrate():
    ''' Demonstrates various features of DoubleLinkedList class. '''
    double_linked_list = DoubleLinkedList(1)
    double_linked_list.insert(2)
    double_linked_list.insert(3)
    double_linked_list.append(4)
    double_linked_list.append(5)

    print(double_linked_list)

    print("\nThe double linked list as iterator:")

    double_linked_list = iter(double_linked_list)

    try:
        print("start:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("prev:", str(double_linked_list.prev()))
        print("next:", str(next(double_linked_list)))
        print("prev:", str(double_linked_list.prev()))
        print("prev:", str(double_linked_list.prev()))
        print("prev:", str(double_linked_list.prev()))
        print("prev:", str(double_linked_list.prev()))
    except StopIteration:
        print("You are reached the begin of the double linked list.")
        double_linked_list = iter(double_linked_list)

    try:
        print("start:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("prev:", str(double_linked_list.prev()))
        print("next:", str(next(double_linked_list)))
        print("prev:", str(double_linked_list.prev()))
        print("prev:", str(double_linked_list.prev()))
        print("next:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("prev:", str(double_linked_list.prev()))
        print("next:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
        print("next:", str(next(double_linked_list)))
    except StopIteration:
        print("You are reached the end of the double linked list.")
        double_linked_list = iter(double_linked_list)

    print("\nThe double linked list as generator:")

    for item in double_linked_list:
        print(str(item), end=' ')

    print('\n')

    double_linked_list.remove_first()

    print(double_linked_list)

    double_linked_list.remove_last()

    print(double_linked_list)

    double_linked_list.remove_first()

    print(double_linked_list)

    double_linked_list.remove_last()

    print(double_linked_list)

    double_linked_list.remove_last()

    print(double_linked_list)

if __name__ == '__main__':
    __demonstrate()
