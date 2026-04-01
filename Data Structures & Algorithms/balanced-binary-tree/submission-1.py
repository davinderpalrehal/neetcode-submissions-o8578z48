# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def calc_height(node, curr):
            if not node:
                return curr
            
            curr += 1
            return max(
                calc_height(node.right, curr),
                calc_height(node.left, curr)
            )
        
        right_height = calc_height(root.right, 1)
        left_height = calc_height(root.left, 1)

        return abs(right_height - left_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)