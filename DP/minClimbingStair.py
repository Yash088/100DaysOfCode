class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        zeroStep = self.climb(cost, 0, {})
        oneStep = self.climb(cost, 1, {})
        return min(zeroStep, oneStep)

    def climb(self, arr, curr, store):

        if curr == len(arr):
            return 0
        if curr > len(arr):
            return 1000
        if curr in store:
            return store[curr]
        step1 = arr[curr] + self.climb(arr, curr+1, store)
        step2 = arr[curr] + self.climb(arr, curr+2, store)

        store[curr] = min(step1, step2)
        return min(step1, step2)
