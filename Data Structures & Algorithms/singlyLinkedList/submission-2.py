class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
    
    def get(self, index: int) -> int:
        curr = self.head.next

        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        
        if not curr:
            return -1

        return curr.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = node
    

    def remove(self, index: int) -> bool:
        curr = self.head.next
        prev = self.head

        for _ in range(index):
            if not curr:
                return False
            prev = curr
            curr = curr.next
        
        if not curr:
            return False

        prev.next = curr.next
        return True


    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
