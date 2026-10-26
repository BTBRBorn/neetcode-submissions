class Solution:
    def dfs(self, image, sr, sc, color, org_color, visited):
        ROWS, COLS = len(image), len(image[0])
        if (min(sr, sc) < 0 or (sr == ROWS or sc == COLS) or
            (sr, sc) in visited or image[sr][sc] != org_color):
            return
        if image[sr][sc] == org_color:
            image[sr][sc] = color
        
        visited.add((sr, sc))
        self.dfs(image, sr+1, sc, color, org_color, visited)
        self.dfs(image, sr-1, sc, color, org_color, visited)
        self.dfs(image, sr, sc+1, color, org_color, visited)
        self.dfs(image, sr, sc-1, color, org_color, visited)
        
        visited.remove((sr, sc))
        return

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_color = image[sr][sc]
        self.dfs(image, sr, sc, color, org_color, set())
        return image
        