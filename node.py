class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def __str__(self):
        return f"Node {self.value} has next: {bool(self.next)}"

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node
