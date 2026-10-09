class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    NUM_NBRS = 4


    def dfs(self, i,j,grid,visited):
        for k in range(self.NUM_NBRS):
            x, y = i+self.dx[k], j+self.dy[k]
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] == '1' and visited[x][y]==0:
                visited[x][y] = 1
                self.dfs(x,y,grid,visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        # Idea: return count of connected components
        rows = len(grid)
        cols = len(grid[0])
        visited: List[List[int]] = [[0]*cols for _ in range(rows)]
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                ans += 1
                visited[i][j] = 1
                self.dfs(i,j,grid,visited)

        return ans
