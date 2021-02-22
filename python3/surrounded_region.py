from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(row: int, col: int):
            if 0 <= row < m and 0 <= col < n and board[row][col] == 'O':
                board[row][col] = 'P'
                dfs(row-1, col)
                dfs(row, col-1)
                dfs(row+1, col)
                dfs(row, col+1)

        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'P':
                    board[i][j] = 'O'


        return