import decorate
import node


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_head_node):
        self._head = new_head_node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, new_tail_node):
        self._tail = new_tail_node

    def push(self, value):
        new_node = node.Node(value)

        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return self.length

    @decorate.print_str
    def pop(self):
        if self.length == 0:
            return 'Empty'

        if self.head == self.tail:
            old_tail = self.head
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next

            old_tail = current_node.next
            self.tail = current_node
            self.tail.next = None

        self.length -= 1
        return old_tail

    def unshift(self, value):
        new_node = node.Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return self.length

    @decorate.print_str
    def shift(self):
        if self.length == 0:
            return 'Empty'
        if self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
        else:
            old_head = self.head
            self.head = self.head.next

        self.length -= 1
        return old_head

    @decorate.print_str
    def find(self, value):
        if value == self.tail.value:
            return self.tail

        current_node = self.head
        while current_node.next is not None:
            if current_node.value == value:
                return current_node
            else:
                current_node = current_node.next
        return -1

    @decorate.print_str
    def replace(self, old_value, new_value):
        new_node = node.Node(new_value)

        if old_value == self.head.value:
            old_node = self.head
            new_node.next = old_node.next
            self.head = new_node
            return old_node

        current_node = self.head
        if old_value == self.tail.value:
            old_node = self.tail

            while current_node.next != self.tail:
                current_node = current_node.next

            current_node.next = new_node
            self.tail = new_node
            return old_node

        while current_node.next is not None:
            if current_node.next.value == old_value:
                old_node = current_node.next
                current_node.next = new_node
                new_node.next = old_node.next
                return old_node
            else:
                current_node = current_node.next

        return -1
