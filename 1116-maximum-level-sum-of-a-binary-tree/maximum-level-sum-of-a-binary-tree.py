from collections import deque
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        level_dict = defaultdict(int)

        def dfs(level,node):
            level_dict[level] += node.val
            if node.right:
                dfs(level + 1, node.right)
            if node.left:
                dfs(level +1, node.left)
        
        dfs(1, root)
        
        return max(level_dict, key=level_dict.get)


        # cur_level = 1
        # max_level = 1
        # max_sum = float('-inf')

        # queue = deque([root])

        # while queue:
        #     cur_sum = 0
        #     cur_nods = len(queue)

        #     for _ in range(cur_nods):
        #         node = queue.popleft()

        #         if node:
        #             cur_sum += node.val
        #         if node.right:
        #             queue.append(node.right)
        #         if node.left:
        #             queue.append(node.left)
                    
        #     if max_sum < cur_sum:
        #         max_sum = cur_sum
        #         max_level = cur_level
                
        #     cur_level += 1

        
        # return max_level
        