# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sub_set = set()
        max_sum = float('-inf')
        total = 0

        def traverse(node):
            nonlocal max_sum, total
            if not node:
                return 0

            left_subtree = traverse(node.left)
            right_subtree = traverse(node.right)
            sub_tree = node.val + left_subtree + right_subtree
            max_sum = max(max_sum, (total-sub_tree) * sub_tree)

            return sub_tree
        
        total = traverse(root)
        traverse(root)
        return max_sum%(10**9 + 7)
        
       # for sub_sum in sub_set:
        #
        