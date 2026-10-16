class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dupes = defaultdict(set)
        col_dupes = defaultdict(set)
        grid_dupes = defaultdict(set) # key = (r/3 , c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_dupes[r] or
                    board[r][c] in col_dupes[c] or
                    board[r][c] in grid_dupes[(r//3, c//3)]):
                    return False
                row_dupes[r].add(board[r][c])
                col_dupes[c].add(board[r][c])
                grid_dupes[(r//3, c//3)].add(board[r][c])
        return True

                


        
        