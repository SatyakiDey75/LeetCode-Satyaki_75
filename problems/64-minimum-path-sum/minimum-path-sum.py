class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # for i in range (m):
        #     for j in range (n):
        #         if i == j == 0:
        #             continue
        #         right_path = down_path = float('inf')
        #         if i != 0:
        #             down_path = grid[i][j] + grid[i-1][j]
        #         if j != 0:
        #             right_path = grid[i][j] + grid[i][j-1]
        #         grid[i][j] = min(down_path, right_path)
        # return grid[m-1][n-1]

        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                lPath = dp[i][j-1]
                uPath = dp[i-1][j]
                if lPath < uPath:
                    dp[i][j] = grid[i][j] + lPath
                else:
                    dp[i][j] = grid[i][j] + uPath

        return dp[m-1][n-1]