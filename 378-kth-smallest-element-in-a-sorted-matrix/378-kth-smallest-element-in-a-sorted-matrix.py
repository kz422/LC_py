class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                l.append(matrix[i][j])
                
        return sorted(l)[k-1]