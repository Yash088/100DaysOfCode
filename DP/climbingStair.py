class Solution:
    def climbStairs(self, n: int) -> int:
        return self.totalWays(0, n, {})

    def totalWays(self, currStep, n, store):
        if(currStep == n):
            return 1
        if(currStep > n):
            return 0
        if(currStep in store):
            return store[currStep]

        oneStep = self.totalWays(currStep+1, n, store)
        twoStep = self.totalWays(currStep+2, n, store)
        store[currStep] = oneStep + twoStep
        return oneStep + twoStep
