from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fruits = 0
        maxminute = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fruits +=1
                if grid[i][j] == 2:
                    queue.append(((i,j), 0))

        def inbounds(tup):
            return tup[0] >= 0 and tup[0] < len(grid) and tup[1] >= 0 and tup[1] < len(grid[0])

        def neighbors(i,j):
            return filter(inbounds, [(i+1,j),(i,j+1),(i-1,j),(i,j-1)])

        while queue:
            e, v = queue.popleft()
            maxminute = max(maxminute, v)
            for i,j in neighbors(e[0], e[1]):
                if grid[i][j] == 1:
                    queue.append(((i,j),v+1))
                    grid[i][j] = 2
                    fruits -= 1
        
        if fruits == 0:
            return maxminute
        return -1
        
            
        
