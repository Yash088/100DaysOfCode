# min number of comparions is  odd:- 3*(n-1)/2 + 1
# even:- 1 + 3*(n-2)/2 

arr = [1,6,2,3,9]
n = len(arr)
max1 = 0
min1 = 0
if( n%2 == 0 ):
    if(arr[0] > arr[1]):
        max1 = arr[0] 
        min1 = arr[1]
    
    else:
        max1 = arr[1]
        min1 = arr[0]
    i = 2
else:
    max1 = arr[0]
    min1 = arr[0]
    i = 1
while i < n-1:
    print(i)
    if(arr[i] > arr[i+1]):
        if(arr[i] > max1):
            max1 = arr[i]
        if(arr[i+1] <min1):
            min1 = arr[i+1]
    else:
        if(arr[i+1] > max1):
            max1 = arr[i+1]
        if(arr[i] < min1):
            min1 = arr[i]
    
    i = i + 2 
print(max1,min1)
