from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        length = 1
        visited.add((0, 0))
        queue.append((0, 0))
        vectors = [(1, 0), (-1, 0), (0, 1), (0, -1),
                     (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft() 
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in vectors:
                    new_r, new_c = r + dr, c + dc
                    if (min(new_r, new_c) < 0 or (new_r == ROWS or new_c == COLS) or
                        grid[new_r][new_c] == 1 or (new_r, new_c) in visited):
                        continue
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
            length += 1
        
        return -1
