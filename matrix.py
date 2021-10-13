# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
arr = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15]
    ]
r=4
c=4
move = 0
top = 0
down = r-1
right = c-1 
left = 0 
count = 0

while (top<=down and left<=right):
    if(move == 0):
        # print("here")
        for i in range(right+1):
            print(arr[top][i])
        top+=1
    elif(move == 1):
        for i in range(top,down+1):
            print(arr[i][right])
        right-=1
    elif(move == 2):
        for i in range(right, left-1, -1):
            print(arr[down][i])
        down-=1
    elif(move == 3):
        for i in range(down, top-1, -1):
            print(arr[i][left])
        left+=1
    move = (move+1)%r
