class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            rowSet = set()
            colSet = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in rowSet:
                        return False
                rowSet.add(board[i][j]) 
                if board[j][i] != '.':
                    if board[j][i] in colSet:
                        return False
                colSet.add(board[j][i]) 
            

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                boxSet = set()
                for i in range(3):
                   for j in range(3):
                    num = board[row + i][col + j]

                    if num != '.':

                        if num in boxSet:
                            return False
                    boxSet.add(num)
        return True



        
        
