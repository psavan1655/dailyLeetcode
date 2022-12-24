class Solution(object):
    def runningSum(self, nums):
        # O(n) time and space complexity
        # result = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         result.append(nums[i])
        #     else:
        #         result.append(result[i - 1] + nums[i])
        # return result

        # O(n) time complexity O(1) Space complexity
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


res = Solution()
print(res.runningSum([3, 1, 2, 10, 1]))
