#!/usr/bin/python3
"""A class Node"""


class Node:
    """class has two attribute"""
    def __init__(self, data, next_node=None):
        """instantiate class Node:
        Args:
            @data: an integer
            @next_node: a node
        """
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """retrieves data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data to value"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrives next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next_node to value"""
        if type(value) is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    """Class for singly linked list"""
    def __init__(self):
        """instantiate class SinglyLinkedList"""
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node

        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            next_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
