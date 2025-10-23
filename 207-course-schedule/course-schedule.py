from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for pre in prerequisites:
            course , prereq = pre
            graph[prereq].append(course)
        
        visited = [0] * numCourses

        def dfs(u): 
            if visited[u] == 1:
                return False
            if visited[u] == 2:
                return True
            visited[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            visited[u] = 2
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True