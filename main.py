class Node:
    """ Node class """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """ Linked list class"""

    def __init__(self):
        self.first_node = None

    def set_first(self, data):
        node = Node(data)
        node.next = self.first_node
        self.first_node = node

    def set_last(self, data):
        node = Node(data)

        if self.first_node is None:
            self.first_node = node
            return

        last = self.first_node

        while last.next:
            last = last.next

        last.next = node

    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

            if not current_node:
                return

        return current_node.data

    def print(self):
        node = self.first_node

        while node is not None:
            print(node.data)
            node = node.next


list = LinkedList()
list.first_node = Node('One')
node2 = Node("Two")
node3 = Node("Three")

list.first_node.next = node2
node2.next = node3

list.set_first("First")
list.set_last("Last")

value = list.read(3)

# while list.node is not None:
#     print(list.node.data)
#     list.node = list.node.next

# list.print()
# print("...")
print(value)
