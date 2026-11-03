"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_nodes = {}

        def deepcopy(node):
            if node in hash_nodes:
                return hash_nodes[node]

            copy = Node(val=node.val, neighbors=[])
            hash_nodes[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(deepcopy(n))

            return copy

        return deepcopy(node) if node else None
        