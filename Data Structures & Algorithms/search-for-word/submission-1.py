class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0]*len(board[0]) for e in board]

        def inbounds(i,j):
            return i< len(board) and i >= 0 and j < len(board[0]) and j >= 0

        def backtrack(i,j, cid): #index of word
            if cid == len(word):
                return True

            found = False
            for sq in [(i+1,j), (i,j+1),(i-1,j),(i,j-1)]:
                if not inbounds(sq[0], sq[1]) or visited[sq[0]][sq[1]]: continue
                if board[sq[0]][sq[1]] == word[cid]:
                    visited[sq[0]][sq[1]] = 1
                    found = found or backtrack(sq[0], sq[1], cid+1)
                    visited[sq[0]][sq[1]] = 0
            return found

        found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    found = found or backtrack(i,j, 1)
                    visited[i][j] = 0
        return found

            