#!/usr/bin/python3
"""Define a class for singly-linked list."""


class Node:
    """represent a single node"""

    def __init__(self, data, next_node=None):
        """initialize a node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """represents class SinglyLinkedList."""

    def __init__(self):
        """Initialize a class"""
        self.__head = None

    def sorted_insert(self, value):
        """insert new node to the class"""

        n = Node(value)
        if self.__head is None:
            n.next_node = None
            self.__head = n

        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n

        else:
            y = self.__head
            while (y.next_node is not None and
                    y.next_node.data < value):
                y = y.next_node
            n.next_node = y.next_node
            y.next_node = n

    def __str__(self):
        """define representation of class"""
        values = []
        y = self.__head

        while y is not None:
            values.append(str(y.data))
            y = y.next_node
        return ("\n".join(values))
