# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m+n) ood for bigger input
        row = 0
        column = len(matrix[0])-1
        n = len(matrix)
        while(row < n and column >= 0):
            if(matrix[row][column] == target):
                return True
            elif(matrix[row][column] > target):
                column -= 1
            else:
                row += 1
        return False

        #  O(log r) + O(log c) not for the bigger inputs
        r = len(matrix)
        if r == 0:
            return False

        c = len(matrix[0])
        r1, r2 = 0, r-1
        while r1 < r2:
            mid = r1 + (r2-r1)//2
            if matrix[mid][c-1] < target:
                r1 = mid+1
            elif matrix[mid][0] > target:
                r2 = mid-1
            else:
                r1 = mid
                break

        c1, c2 = 0, c-1
        while c1 <= c2:
            mid = c1 + (c2-c1)//2
            if matrix[r1][mid] < target:
                c1 = mid+1
            elif matrix[r1][mid] > target:
                c2 = mid-1
            else:
                return True

        return False
