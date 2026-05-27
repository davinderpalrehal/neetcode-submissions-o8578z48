class Node:
    def __init__(self, left_idx: int, right_idx: int, total: int):
        self.total = total
        self.left = None
        self.right = None
        self.left_idx = left_idx
        self.right_idx = right_idx

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, arr, left_idx, right_idx):
        if left_idx == right_idx:
            return Node(left_idx, right_idx, arr[left_idx])
        
        mid_idx = left_idx + ((right_idx - left_idx) // 2)
        root = Node(left_idx, right_idx, 0)
        root.left = self.build(arr, left_idx, mid_idx)
        root.right = self.build(arr, mid_idx + 1, right_idx)
        root.total = root.left.total + root.right.total
        return root
    
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)
    
    def update_helper(self, node, index, val):
        if node.left_idx == node.right_idx:
            node.total = val
            return
        
        mid_idx = node.left_idx + ((node.right_idx - node.left_idx) // 2)
        if index > mid_idx:
            self.update_helper(node.right, index, val)
        else:
            self.update_helper(node.left, index, val)
        node.total = node.left.total + node.right.total
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)
    
    def query_helper(self, node, left_idx, right_idx):
        if node.left_idx >= left_idx and node.right_idx <= right_idx:
            return node.total
        
        if node.right_idx < left_idx or node.left_idx > right_idx:
            return 0
        
        return (
            self.query_helper(node.left, left_idx, right_idx) +
            self.query_helper(node.right, left_idx, right_idx)
        )
