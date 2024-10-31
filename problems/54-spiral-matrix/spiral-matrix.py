class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        right, down, left, up = 0, 1, 2, 3
        dire = right
        right_wall, down_wall = n, m
        left_wall, up_wall = -1, 0

        while len(ans) != n*m:
            if dire == right:
                while j < right_wall:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                right_wall -= 1
                dire = down
            elif dire == down:
                while i < down_wall:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                down_wall -= 1
                dire = left
            elif dire == left:
                while j > left_wall:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                left_wall += 1
                dire = up
            else:
                while i > up_wall:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                up_wall += 1
                dire = right
        return ans
