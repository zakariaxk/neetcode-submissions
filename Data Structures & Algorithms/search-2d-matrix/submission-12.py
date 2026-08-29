class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) - 1

        l = 0
        r = len(matrix[0]) - 1

        while top <= bottom:
            row = top + (bottom - top) // 2

            if (matrix[row][0] <= target and target <= matrix[row][-1]):
                while l<=r: 
                    mid = l + (r - l) // 2

                    if matrix[row][mid] == target:
                        return True
                    if matrix[row][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            
            elif(matrix[row][0] > target):
                bottom = row - 1

            else:
                top = row + 1
        
        return False