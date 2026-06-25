# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        bigger, smaller = None, None
        if p.val > q.val:
            bigger = p.val
            smaller = q.val
        else:
            bigger = q.val
            smaller = p.val
        
        curr = root

        while curr:
            if curr.val <= bigger and curr.val >= smaller:
                return curr
            
            if curr.val > bigger:
                curr = curr.left
            else:
                curr = curr.right
        

