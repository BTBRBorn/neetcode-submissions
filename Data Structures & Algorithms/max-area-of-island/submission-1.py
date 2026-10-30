from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            queue = deque()
            area = 0
            vectors = ((1, 0), (-1, 0), (0, 1), (0, -1))
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    area += 1
                    for dr, dc in vectors:
                        new_r, new_c = r + dr, c + dc
                        if (min(new_r, new_c) < 0 or (new_r == ROWS or new_c == COLS) or
                            grid[new_r][new_c] == 0 or (new_r, new_c) in visited):
                            continue
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            return area

        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0 
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = bfs(r, c)
                    if area > max_area:
                        max_area = area
        
        return max_area
        