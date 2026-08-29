class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target == matrix[i][j]:
                    return True
        return False
        # l = 0
        # r = len(matrix[0])

        # row = 0
        # col = 0
        
        # while l<=r:
        #     mid = l + (r - l) // 2
        #     if target == matrix[l][mid]:
        #         return True

        # for i in range(len(matrix)):
        #     if target == matrix[l][i]:
        #         return True
        #     if target >

            

        