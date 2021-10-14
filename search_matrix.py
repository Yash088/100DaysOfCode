# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

row = 4
column = 4 
r = 0
c = 0
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
left = 0
right = (row*column)-1
element = 16
# For total:- 16
# 4 7 8 10
# For toal 15:-
# 6 7 9 10 16
middle = (left + right)//2 
while True: 
    c = middle%column
    r = middle//row
    print("Cordinate:")
    print(r,c)
    if(arr[r][c] > element):
        print("Element is small:")
        print(r,c)
        middle = (left + middle)//2
        print("New middle")
        print(middle)
    elif(arr[r][c] < element ):
        print("Element is greater:")
        print(r,c)
        middle = (middle + right)//2
        print("New middle")
        print(middle)

    elif(arr[r][c] == element):
        print("Found Element")
        print(r,c)
        break        
    else:
        print("Not Present")
        break        
print("Hello world")
