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
            
        def get_height(node, curr):
            if not node:
                return curr
            
            return max(get_height(node.left, curr + 1), get_height(node.right, curr + 1))

        left_height = get_height(root.left, 1)
        right_height = get_height(root.right, 1)

        if abs(left_height - right_height) > 1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)