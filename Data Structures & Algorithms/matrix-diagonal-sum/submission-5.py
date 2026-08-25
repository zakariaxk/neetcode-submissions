class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        j = len(mat) - 1

        for i in range(len(mat)):
            if i == j:
                total += mat[i][i]
            else:
                total += mat[i][i]
                total += mat[i][j]

            j -= 1

        return total