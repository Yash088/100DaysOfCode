# Remove element with the memory of O(1). the result be placed in the first part of the array.
def removeElement(nums, val):
    l = len(nums)
    j = 0
    for i in range(l):
        if(nums[i] != val):
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return j


print(removeElement([3, 2, 2], 2))
