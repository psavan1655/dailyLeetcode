class Solution(object):
    def pivotIndex(self, nums):
        # leftSum = 0
        # rightSum = sum(nums)
        # for i in range(len(nums)):
        #     rightSum -= nums[i]
        #     if leftSum == rightSum:
        #         return i
        #     leftSum += nums[i]
        # return -1

        numsTotal = 0
        for i in range(0, len(nums)):
            numsTotal += nums[i]

        runningSum = 0
        for i in range(0, len(nums)):
            runningSum = runningSum + nums[i]
            if (runningSum) == numsTotal - runningSum + nums[i]:
                return i

        return -1


res = Solution()
print(res.pivotIndex([1, 7, 3, 6, 5, 6]))
