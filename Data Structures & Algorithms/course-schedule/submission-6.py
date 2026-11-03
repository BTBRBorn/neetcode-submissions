from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for p, c in prerequisites:
            if c not in adjList:
                adjList[c] = []
            if p not in adjList:
                adjList[p] = []
            adjList[p].append(c)

        def dfs(node, path):
            if node in path:
                return False

            if node in memo:
                return memo[node]

            path.add(node) 
            can_finish = True
            for c in adjList[node]:
                can_finish = dfs(c, path)
                if not can_finish:
                    break
            path.remove(node)
            memo[node] = can_finish

            return can_finish
            
        memo = {}
        for p, c in prerequisites:
            can_finish = dfs(p, set())
            if not can_finish:
                return False
        return True



