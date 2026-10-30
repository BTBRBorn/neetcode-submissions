#Efficient bfs: O(n*m)
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            vectors = ((1, 0), (-1, 0), (0, 1), (0, -1))
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in vectors:
                        new_r, new_c = r + dr, c + dc
                        if (min(new_r, new_c) < 0 or (new_r == ROWS or new_c == COLS) or
                            grid[new_r][new_c] == "0" or (new_r, new_c) in visited):
                            continue
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
                
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands

        