class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            if target<=matrix[i][m-1]:
                if target in matrix[i]:
                    return True
                return False
        return False
    
#As it is sorted matrix, check which row's end element is greater than equal to target element. That row might be the answe if target present in that row

        