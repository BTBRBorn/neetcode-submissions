from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        fresh = set()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                if grid[r][c] == 2:
                    rottens.append((r, c))
        visited = set()
        queue = deque()
        vectors = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r, c in rottens:
            visited.add((r, c))
            queue.append((r, c))
        if not fresh:
            return 0
        minutes = 0
        while queue:
            if not fresh:
                return minutes
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in vectors:
                    new_r, new_c = r + dr, c + dc
                    if (min(new_r, new_c) < 0 or (new_r == ROWS or new_c == COLS) or
                        (grid[new_r][new_c] == 0 or grid[new_r][new_c] == 2) or
                         (new_r, new_c) in visited):
                        continue  
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
                    fresh.remove((new_r, new_c))
                    grid[new_r][new_c] = 2
            minutes += 1

        return -1