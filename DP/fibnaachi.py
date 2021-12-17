class Solution:
    def fib(self, n: int, arr=[0, 1]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > len(arr):
            return arr[n]
        res = self.fib(n-1) + self.fib(n-2)
        arr.append(res)
        return res
        # arr=[0,1]
        # i=2
        # while n >= i:
        #     arr.append(arr[i-1]+arr[i-2])
        #     i = i+1
        # return arr[n]
