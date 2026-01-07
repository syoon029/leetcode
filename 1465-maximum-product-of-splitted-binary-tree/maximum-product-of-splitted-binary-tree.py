# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sub_set = set()
        max_sum = float('-inf')

        def traverse(node):
            if not node:
                return 0

            left_subtree = traverse(node.left)
            right_subtree = traverse(node.right)
            sub_tree = node.val + left_subtree + right_subtree
            sub_set.add(sub_tree)

            return sub_tree
        
        total = traverse(root)
        print(total)
        
        for sub_sum in sub_set:
            max_sum = max(max_sum, (total - sub_sum) * sub_sum)
            
        return max_sum  % (10**9+7)