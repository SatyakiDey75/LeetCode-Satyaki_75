def solveNQueens(board, col, N, solutions):
    if col == N:
        solutions.append([''.join('Q' if cell == 1 else '.' for cell in row) for row in board])
        return
    
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            solveNQueens(board, col + 1, N, solutions)
            board[i][col] = 0

def isSafe(board, row, col, N):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [[0 for x in range(n)] for y in range(n)]
        # solutions = []
        # solveNQueens(board, 0, n, solutions)
        # return solutions

        # for beats :)
        res = []
        cols = set()
        pos = set()
        neg = set()
        def solveRow(queens, row):
            if row == n:
                res.append(queens.copy())
            for col in range(n):
                if col in cols or row + col in pos or row - col in neg:
                    continue
                cols.add(col)
                pos.add(row + col)
                neg.add(row - col)

                curr = ["."] * n
                curr[col] = "Q"
                queens[row] = "".join(curr)
                solveRow(queens, row+1)

                cols.remove(col)
                pos.remove(row + col)
                neg.remove(row - col)
        solveRow([""]*n, 0)
        return res