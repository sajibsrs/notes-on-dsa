# Singly linked list

Generally linked list refers to singly linked list. While arrays and linked list has many similarities, there are some big different under the hood. Items in a linked list is not contiguous block of memory like arrays. They can be scattered across different memory locations.

> // TODO: add graphical explanation

Items of linked lists are called nodes. Each node consists of **value** and **link** to the next node. **Link** is the memory address of the next item. The last node has a **link** to _NULL_ as it has no next element.

> A linked list's first and last node can be also referred as head and tail respectively.

## Creating linked list

```python
# creating linked list in python


class Node:
    """ Node class """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """ Linked list class"""

    def __init__(self):
        self.first_node = None


list = LinkedList()
list.first_node = Node("One")
node2 = Node("Two")
node3 = Node("Three")

list.first_node.next = node2
node2.next = node3

current_node = list.first_node
# print the node values
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
```

### Results for code above:

```text
One
Two
Three
```

## Traversing linked list

```python
# traversing linked list in python


class Node:
    """ Node class """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """ Linked list class"""

    def __init__(self):
        self.first_node = None

    def print(self):
        node = self.first_node

        while node is not None:
            print(node.data)
            node = node.next


list = LinkedList()
list.first_node = Node("One")
node2 = Node("Two")
node3 = Node("Three")

list.first_node.next = node2
node2.next = node3

list.print()
```

### Results for code above:

```text
One
Two
Three
```

## Insertion at the beginning of a linked list

```python
# insertion at the beginning in python


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

    def print(self):
        node = self.first_node

        while node is not None:
            print(node.data)
            node = node.next


list = LinkedList()
list.first_node = Node("One")
node2 = Node("Two")
node3 = Node("Three")

list.first_node.next = node2
node2.next = node3

list.set_first("First")

list.print()
```

### Results for code above:

```text
First
One
Two
Three
```

## Insertion at the end of a linked list

```python
# insertion at the end in python


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

    def print(self):
        node = self.first_node

        while node is not None:
            print(node.data)
            node = node.next


list = LinkedList()
list.first_node = Node("One")
node2 = Node("Two")
node3 = Node("Three")

list.first_node.next = node2
node2.next = node3

list.set_first("First")
list.set_last("Last")

list.print()
```

### Results for code above:

```text
First
One
Two
Three
Last
```

## Reading from a linked list

```python
# reading from a linked list in python


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

print(value)
```

### Results for code above:

```text
Three
```

> // TODO: add search
>
> // TODO: add efficiency
>
> // TODO: add performance table

