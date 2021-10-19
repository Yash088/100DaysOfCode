#User function Template for python3
# This will take O(nlogm) as n is row traversal we are doing inside the rowWithMax1s and logm for bianry_search
class Solution:

	def binary_search( self, arr):    
        left = 0
        right = len(arr) - 1
        target  = 1
        while right >= left:
            mid = (left + right)//2
            
#             You can also do the conditioning of arr[mid]==0 than move to right else to left as it is sorted array and moreover 
#             binary so only two values will be there
            if((mid == 0 or arr[mid-1] == 0 ) and arr[mid] == target):
                return mid
                    
            elif(arr[mid] > target or (arr[mid] == 1 and arr[mid-1] == 1 )):
                right = mid - 1
                
            else: 
                left = mid + 1
        return -1

	def rowWithMax1s(self,arr, n, m):
		# code here
        max_1 = 0
        max_row_index = -1
        for i in range(n):
            val = self.binary_search(arr[i])
            if(val != -1 and m-val > max_1):
                max_1 = m-val
                max_row_index = i
            
        return max_row_index

# More effecient approach :




