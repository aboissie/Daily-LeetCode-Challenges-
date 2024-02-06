from typing import List

class Solution:
    @staticmethod
    def distance(cell1, cell2):
        """
        Returns the distance between two cells 
        """
        return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])
    
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        Given the `rows` and `cols` of a matrix and the `rCenter` and `cCenter` representing the row and column where the 
        center of the matrix is located, return a list of all cells in the matrix, sorted in increasing order by the distance 
        from the center of the matrix.
        """
        return sorted([[i, j] for i in range(rows) for j in range(cols)], key=lambda x: self.distance(x, [rCenter, cCenter]))
    
if __name__ == '__main__':
     rows = 2
     cols = 3
     rCenter = 1
     cCenter = 2

     print(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter))