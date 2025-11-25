class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wl = len(word)

        def dfs(rows, cols, i):
            if i == wl:
                return True
            if rows < 0 or rows >= m or cols < 0 or cols >= n:
                return False
            if board[rows][cols] != word[i]:
                return False

            tmp = board[rows][cols]
            board[rows][cols] = None

            if dfs(rows+1, cols, i+1) or dfs(rows-1, cols, i+1) or dfs(rows, cols+1, i+1) or dfs(rows, cols-1, i+1):
                board[rows][cols] = tmp
                return True

            board[rows][cols] = tmp
            return False

        for rows in range(m):
            for cols in range(n):
                if dfs(rows, cols, 0):
                    return True

        return False