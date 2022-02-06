# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] + nums[j] == target ):
#                     return [i,j]

class Solution:
    def twoSum(self, nums, target):
        hashedDict = {}
        for i in range(len(nums)):
            if (hashedDict.get(target - nums[i]) != None):
                return [i, hashedDict.get(target - nums[i])]
            hashedDict[nums[i]] = i


ret = Solution()
print(ret.twoSum([2,7,11,15], 9))