 

N = 4
 


def findMax (arr):

    row = 0

    j = N - 1

    for i in range(0, N):

        # find left most position

        # of 1 in a row find 1st

        # zero in a row

        while (arr[i][j] == 1

                     and j >= 0):

            row = i

            j -= 1

         

    print("Row number = " , row + 1,

         ", MaxCount = ", N - 1 - j)
 
# driver program

arr = [ [0, 0, 0, 1],

        [0, 0, 0, 1],

        [0, 0, 0, 0],

        [0, 1, 1, 1] ]

         
findMax(arr)
