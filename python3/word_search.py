from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word)

        def exist_recursion(i: int, j: int, k: int, mem: set) -> bool:
            if board[i][j] == word[k]:
                new_mem = set(mem)
                new_mem.add((i, j))
                return k == l-1 \
                       or (0 <= i-1 < m and (i-1, j) not in mem and exist_recursion(i-1, j, k+1, new_mem)) \
                       or (0 <= i+1 < m and (i+1, j) not in mem and exist_recursion(i+1, j, k+1, new_mem)) \
                       or (0 <= j-1 < n and (i, j-1) not in mem and exist_recursion(i, j-1, k+1, new_mem)) \
                       or (0 <= j+1 < n and (i, j+1) not in mem and exist_recursion(i, j+1, k+1, new_mem))
            else:
                return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and exist_recursion(r, c, 0, set()):
                    return True
        return False