class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def inbounds(e):
            return e[0] >= 0 and e[1] >= 0 and e[0] < len(grid) and e[1] < len(grid[0])
        def neighbors(i,j):
            return filter(inbounds, [(i+1,j), (i,j+1), (i-1,j), (i,j-1)])

        def bfs(i,j,depth):
            queue = deque([(i,j,depth)])
            visited = set((i,j))
            while queue:
                i, j, d = queue.popleft()
                if grid[i][j] != -1 and (i,j) not in visited:
                    grid[i][j] = min(grid[i][j], d)
                    visited.add((i,j))
                    for e in neighbors(i,j):
                        queue.append((e[0], e[1], d+1))
                    
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i,j,0)
