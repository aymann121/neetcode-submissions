class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for column in row:
                if column in rowSet:
                    return False
                elif column != ".":
                    rowSet.add(column)
        for i in range(9):
            columnSet = set()
            for j in range(9):
                if board[j][i] in columnSet:
                    return False
                elif board[j][i] != ".":
                    columnSet.add(board[j][i])

        for i in range(3):
            for j in range(3):
                boxSet = set()
                for k in range(3):
                    for l in range(3):
                        if board[k  + 3 * i][l + 3*j] in boxSet:
                            return False
                        elif board[k  + 3 * i][l + 3*j]!= ".":
                            boxSet.add(board[k  + 3 * i][l + 3*j])
        
        return True