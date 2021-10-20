# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# insertion sort start with 1 ... len(arr) because in the insertion sort you have one sorted array for traverse. 
# get the key and go till i-1 to 0 till the element of the array is greater than the current key so that you can get the array index to insert
# while traversing backward you have to swap the element so that you can insert at the index as we have done in the line no. 9. than you have the index insert at the j+1 and Bingo :)
arr = [64, 25, 12, 22, 11]
n= len(arr)
for i in range(1,n):
    key = arr[i]
    j= i-1
    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        print(arr)
        j-=1
    arr[j+1] = key
print(arr)
