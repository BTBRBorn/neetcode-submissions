from collections import deque
class Graph:
    
    def __init__(self):
        self.adjSet = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjSet:
            self.adjSet[src] = set()
        if dst not in self.adjSet:
            self.adjSet[dst] = set()
        if dst not in self.adjSet[src]:
            self.adjSet[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjSet and dst in self.adjSet[src]:
            self.adjSet[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque()
        visited = set()
        queue.append(src)
        visited.add(src)

        while queue:
            node = queue.popleft()
            for c in self.adjSet[node]:
                if c == dst:
                    return True
                if c not in visited:
                    visited.add(c)
                    queue.append(c)
        
        return False
