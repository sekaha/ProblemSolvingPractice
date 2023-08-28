# we can use sets for each things,,,
class Solution:
    def isValidSudoku(self, board):
        # Domain specific solution, because there are 9 rows and columns and 9 partitions
        for i in range(9):
            # validate row
            occurences = []

            for v in board[i]:
                # it can't be valid, because a number is used more than once
                if v in occurences:
                    print("row error")
                    return False

                # this is blank space
                if v!=".":
                    occurences.append(v)
        
            # validate column
            occurences = []

            for j in range(9):
                v = board[j][i]

                # it can't be valid, because a number is used more than once
                if v in occurences:
                    print("col error")
                    return False

                # this is blank space
                if v!=".":
                    occurences.append(v)
            
            # validate section
            occurences = []

            for j in range(9):
                x_off = (i*3 % 9) + j%3
                y_off = (i*3 // 9)*3 + j//3

                v = board[x_off][y_off]
                
                if v in occurences:
                    print("section error")
                    return False

                # this is blank space
                if v!=".":
                    occurences.append(v)

        return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()

print(sol.isValidSudoku(board))