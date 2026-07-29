class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
 
        def checkRows():
            valid = True
            for i in range(len(board)):
                
                numbers = []
                for j in range(len(board[i])):
                    if board[i][j] != '.':
                        numbers.append(board[i][j])
                if len(numbers) != len(set(numbers)):
                    valid = False
            return valid
        
        def checkCols():
            valid = True
            for j in range(len(board[0])):
                numbers = []
                for i in range(len(board)):
                    if board[i][j] != '.':
                        numbers.append(board[i][j])
                if len(numbers) != len(set(numbers)):
                    valid = False
            return valid

        def checkSquare(p1, p2):
            numbers = []
            for i in range(p1, p1+3):
                for j in range(p2, p2+3):
                    if board[i][j] != '.':
                        numbers.append(board[i][j])
            return len(numbers) == len(set(numbers))

        def checkSquares():
            valid = True
            for i in range(0, 7, 3):
                for j in range(0, 7, 3):
                    if not checkSquare(i,j):
                        valid = False
            return valid
        return checkSquares() and checkCols() and checkRows()