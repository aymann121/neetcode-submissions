class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = [[0]*len(grid[0]) for _ in grid]


        def inbounds(i,j):
            return i< len(grid) and i >= 0 and j< len(grid[i]) and j >= 0

        def searchFrom(i,j):
            if (not inbounds(i,j)) or visited[i][j] or grid[i][j] == 0: return 0
            visited[i][j] = 1
            res = 1
            for e in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                res += searchFrom(e[0], e[1])
            return res
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]: continue
                if grid[i][j] == 0: continue

                maxArea = max(maxArea, searchFrom(i,j))
        return maxArea
                