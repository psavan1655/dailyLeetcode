def maxSubArray(nums):
    maximum = float('-inf')
    current = 0
    for i in range(len(nums)):
        if(current >= 0):
            current = current + nums[i]
        else:
            current = nums[i]
        if(current > maximum):
            maximum = current
    return maximum


print(maxSubArray([-1]))
