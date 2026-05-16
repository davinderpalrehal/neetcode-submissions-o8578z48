class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        node = Node(value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def appendleft(self, value: int) -> None:
        node = Node(value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        
        val = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1

        return val

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        
        val = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1

        return val
