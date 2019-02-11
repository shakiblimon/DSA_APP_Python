__version__ = "V1.0.0"
__author__ = "Shakib Limon"

'''
Single Linked List

A single linked list contains an item and reference to the next item .

'''


'''
Creating  Node Class
'''

class Node :
    def __init__(self,data):
        """
        :param data:

        node class will contain two member variables item and ref
        """
        self.item = data
        self.ref = None



'''
    Creating the Single Linked List Class
'''
class LinkedList:
    def __init__(self):
        """

        """
        self.start_node = None

#   Traversing Linked List Items
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

#   Insert at the first position of Node
    def insert_at_start(self,data):
        """
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node

    #   Insert at the last position of the node
    def insert_at_end(self,data):
        """
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node

        while n.ref is not None:
            n = n.ref
        n.ref = new_node

#       Insert after intem

    def insert_after_item(self,x,data):
        """
        :param x:
        :param data:
        :return:
        """
        n= self.start_node
        print(n.ref)
        while n is not  None:
            if n.item == x:
                break
            n=n.ref
        if n is None:
            print('Item not in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
