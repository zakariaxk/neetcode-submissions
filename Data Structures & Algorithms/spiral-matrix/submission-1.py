class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        res = []

        while top <= bottom and left <= right:
            # go left -> right across top
            for col in range(left, right + 1):
                res.append(matrix[top][col])

            # move top down
            top += 1

            # go top -> bottom down right side
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])

            # move right left
            right -= 1

            # go right -> left across bottom
            # only if top <= bottom
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
            # move bottom up
            bottom -= 1

            # go bottom -> top up left side
            # only if left <= right
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])

            # move left right
            left += 1

        return res