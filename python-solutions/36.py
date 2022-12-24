# class Solution():
#     def isValidSudoku(self, board):
        # print(board)
        # col1 = {}
        # col2 = {}
        # col3 = {}
        # col4 = {}
        # col5 = {}
        # col6 = {}
        # col7 = {}
        # col8 = {}
        # col9 = {}

        # grid1 = {}
        # grid2 = {}
        # grid3 = {}
        # grid4 = {}
        # grid5 = {}
        # grid6 = {}
        # grid7 = {}
        # grid8 = {}
        # grid9 = {}
        # for i in range(len(board)):
        #     row = {}
        #     for j in range(len(board)):
        #         if (j == 0):
        #             if(board[i][j] in col1):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col1[board[i][j]] = True
        #         if (j == 1):
        #             if(board[i][j] in col2):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col2[board[i][j]] = True
        #         if (j == 2):
        #             if(board[i][j] in col3):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col3[board[i][j]] = True
        #         if (j == 3):
        #             if(board[i][j] in col4):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col4[board[i][j]] = True
        #         if (j == 4):
        #             if(board[i][j] in col5):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col5[board[i][j]] = True
        #         if (j == 5):
        #             if(board[i][j] in col6):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col6[board[i][j]] = True
        #         if (j == 6):
        #             if(board[i][j] in col7):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col7[board[i][j]] = True
        #         if (j == 7):
        #             if(board[i][j] in col8):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col8[board[i][j]] = True
        #         if (j == 8):
        #             if(board[i][j] in col9):
        #                 return False
        #             elif board[i][j] != '.':
        #                 col9[board[i][j]] = True

        #         if (j >= 0 and j<3 and i>=0 and i<3):
        #             if(board[i][j] in grid1):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid1[board[i][j]] = True

        #         if (j >= 3 and j<6 and i>=3 and i<6):
        #             if(board[i][j] in grid2):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid2[board[i][j]] = True
                
        #         if (j >= 6 and j<9 and i>=6 and i<9):
        #             if(board[i][j] in grid3):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid3[board[i][j]] = True

        #         if (j >= 0 and j<3 and i>=3 and i<6):
        #             if(board[i][j] in grid4):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid4[board[i][j]] = True

        #         if (j >= 0 and j<3 and i>=6 and i<9):
        #             if(board[i][j] in grid5):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid5[board[i][j]] = True

        #         if (j >= 3 and j<6 and i>=0 and i<3):
        #             if(board[i][j] in grid6):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid6[board[i][j]] = True
                
        #         if (j >= 3 and j<6 and i>=6 and i<9):
        #             if(board[i][j] in grid7):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid7[board[i][j]] = True
                
        #         if (j >= 6 and j<9 and i>=0 and i<3):
        #             if(board[i][j] in grid8):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid8[board[i][j]] = True
                
        #         if (j >= 6 and j<9 and i>=3 and i<6):
        #             if(board[i][j] in grid9):
        #                 return False
        #             elif board[i][j] != '.':
        #                 grid9[board[i][j]] = True
                
        #         if(board[i][j] in row):
        #             return False
        #         elif board[i][j] != '.':
        #             row[board[i][j]] = True
        # return True

class Solution():
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'), [])
        return len(seen) == len(set(seen))

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
ret = Solution()
print(ret.isValidSudoku(board))
