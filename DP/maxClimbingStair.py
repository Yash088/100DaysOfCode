def maxStair(arr):
    step0 = climbingStep(arr, 0, len(arr), {})
    step1 = climbingStep(arr, 1, len(arr), {})
    return max(step0, step1)


def climbingStep(arr, currStep, top, dp):
    if currStep == top:
        return 0
    if currStep > top:
        return -1
    if currStep in dp:
        return dp[currStep]
    step1 = arr[currStep] + climbingStep(arr, currStep+1, top, dp)
    step2 = arr[currStep] + climbingStep(arr, currStep+2, top, dp)
    dp[currStep] = max(step1, step2)
    return max(step1, step2)


# print(maxStair([10, 15, 20]))
print(maxStair([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(sum([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
