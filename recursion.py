# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# https://www.geeksforgeeks.org/types-of-recursions/ artical
# O(N)
# Tail Recursion means Tail to head 5 ----- 1
# When recurion call is the last in the funciton before that we are executing any operation 
def Count(n):
    # Base Case
    if(n==0):
        return
    #Work
    print(n)
    #recursion
    Count(n-1)
Count(5)
# Head Recursion means Head to Tail 1 ----- 5 moreover When recurion call is the first in the funciton after that we are executing any operation 
#  It is printing dfrom 1--- 5 because first we are making call than will get a return and pointer will execute next print statement after getting return
# Count(5) Print --Count(4) Print--Count(3) Print-Count(2) Print--Count(1) Print--Count(0) return 
# after the count has return -- Count(1) got return execute next instruction of print --
# Count(2) got return execute next instruction of print --Count(3) got return execute next iinstruction of print --Count(4) got return execute next instruction of print
def Count(n):
    if(n == 0):
        return
    Count(n-1)
    print(n)
Count(5)

# Factorial
# Time Complexity:- O(n)
# Space Complexity:- O(n)
# Head Recursion
def Factorial(n):
    if n==1:
        return 1
    return n * Factorial(n-1)
print(Factorial(6))


# Fibanachi Series
# See recursion tree 
def Fab(n):
    if(n==0 or n==1):
        return n
    return Fab(n-1) + Fab(n-2)
print(Fab(12))


# Counting in English
# Head Recursion
# TC:- O(Length of Numbers)
# SC:- O(Length of Numbers)
arr = ["Zero","One","two","Three", "Four","Five","Six","Seven","Eight","Nine"]
def Word(n):
    if n == 0:
        return 
    # Word(n//10)
    # print(arr[n%10],end="") 
    return str(Word(n//10))  + arr[n%10] 
print(Word(12))



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Exponent
# TC:- O(Power)
# SC:- O(Power)
def Power(num,power):
    if power == 0:
        return 1
    return num * Power(num,power-1)

# TC:- O(log(Power))
# SC:- O(log(Power))
# 4    2*2 2*1*!   1    
4 - 2 - 1 - 0

def FastPower(num,power):
    if power == 0:
        return 1
    ans = FastPower(num,power//2)
    if( power%2 > 0):
        return num * ans * ans 
    else:
        return ans *ans
        
print(FastPower(2,4))   

# Sorted/Unsorted
# 5 64
# 4 48
# 3 20
# 2 11
# 1 10
# 0 9
# T.C:- O(n)
# S.C.:- O(n)
def sort(arr,n):
    if n==0:
        return True 
    elif(arr[n] >= arr[n-1]):
        return sort(arr,n-1)
        
    else:
        return False
print(sort([9,11,11,22,23,64],5))
#Subsequance
res = []
def subset(arr,n):
    if n == len(arr)-1:
        return res.append(arr[n])
    ans = subset(arr,n+1)
    for i in range(0,len(res)):
        res.append(arr[n]+res[i])
    res.append(arr[n])
    return res
# 3
# 2  
# 1   [d]ans = d c == c,d,cd
# 0   d 
ty = subset(['a','b','c','d'],0)
ty.sort()
print(ty)
