# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Bubble Sort:- replacing the biggest bubble at the end of the array by making swaps. 
# time Complexity:- O(n^2)
# For sorted it is O(n) as we can have a swap = False at the outer loop if no swaps occurs at the first pass it means array is already sorted.

arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if(arr[j] > arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            print(arr)

print(arr)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Simply sorting by making leaste value at the start of the array every time. same as selection sort selecting and picking.
# arr = [64, 25, 12, 22, 11]
# n = len(arr)

# for i in range(n):
#     for j in range(i+1,n):
#         if(arr[i] > arr[j]):
#             arr[i],arr[j] = arr[j],arr[i]
