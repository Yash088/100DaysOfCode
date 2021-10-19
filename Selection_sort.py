# we have choose index for min not the value like min = arr[i] because we have to swap the index and if choose min than we can't find the jth index from whihch we hvae to replace
# because at every iteration of i j we are moving till the end of the array. one other can be to have another variable that store j index of the minest value 
# The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation. 
arr = [64, 25, 12, 22, 11]
n = len(arr)
for i in range(n):
    min = i
#   min = arr[i]
#   min_j = -1
    for j in range(i+1,n):
        if (arr[j] <  arr[min] ):
#       if (arr[j] <  min ):
            min = j
#           min = arr[j]
#           min_j = j
    arr[i], arr[min] = arr[min], arr[i]
#        arr[i], arr[min_j] = arr[min_j], arr[i]


print(arr)
