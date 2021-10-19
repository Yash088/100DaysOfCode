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
# For this time complexity wil lbe  O(mn) but if you see we are not traversing the inner loop if we have  0 so we are traversing only for one.
# For a testacsse liek this. 
# arr = [[0, 0, 0, 1], it wil ltraverse last column once and else it will countinue only outer loop not the inner for the test case with only 0 it will still traverse only the 
#        [0, 0, 0, 1],  row it will neveer start the inner loop but for the testcase where everything is one it will only traverse the first  row  + column and only  
#        [0, 0, 0, 1],  the column 0 coz at the first pass we will be at the index 0 so we can have a if and check if the curr_coulmn is 0 and we have one so we can break the 
#        [0, 0, 0, 1]] outer loop so that if only if it is constraints to print least row number.

arr = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
 
max_1 = 0 
max_row_index = 0
n = len(arr)
m = len(arr[0])
curr_col = m-1
for i in range(n):
    while(curr_col >=0 and arr[i][curr_col] == 1):
        curr_col -= 1
        max_row_index = i
        
print(max_row_index)



