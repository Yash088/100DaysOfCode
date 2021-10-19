# Simply two end point left and right according to the middle element we traverse either left or right coz array is sorted.


arr = [1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(arr) - 1
target  = 9
while right > left:
    mid = (left + right)//2
    if(arr[mid] > target):
        right = mid -1
    elif(arr[mid] == target):
        print(target,mid)
        break
    else: 
        left = mid + 1
