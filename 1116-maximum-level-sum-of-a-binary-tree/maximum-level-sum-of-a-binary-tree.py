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
        #BFS
        # queue = deque([root])
        # max_sum = float('-inf')
        # max_lev = 1
        # cur_lev = 1

        # while queue:
        #     cur_nodes = len(queue)
        #     cur_sum = 0

        #     for i in range(cur_nodes):
        #         nod = queue.popleft()
        #         cur_sum += nod.val

        #         if nod.left:
        #             queue.append(nod.left)
        #         if nod.right:
        #             queue.append(nod.right)
                
        #     if cur_sum > max_sum:
        #         max_sum = cur_sum
        #         max_lev = cur_lev
            
        #     cur_lev += 1
                

        # return max_lev

        #recursion
        levels = defaultdict(int)
        def sum_val(depth,root):
            if root:
                levels[depth] += root.val
                sum_val(depth+1, root.left)
                sum_val(depth+1, root.right)
        
        sum_val(1,root)
        return max(levels, key=levels.get)

        