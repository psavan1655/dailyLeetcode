#===================================================== Solution 1 =========================================================
class Solution(object):
    def containsDuplicate(self, nums):
        tmp = set()
        for i in range(len(nums)):
            if nums[i] in tmp:
                return True
            tmp.add(nums[i])
        return False

#===================================================== Solution 2 =========================================================
class Solution(object):
    def containsDuplicate(self, nums):
        if (len(set(nums)) != len(nums)):
            return True
        return False

#===================================================== Solution 3 =========================================================
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False