class Solution(object):
    def search(self, nums, target):
        lptr = 0
        rptr = len(nums) - 1
        while lptr <= rptr:
            idx = (lptr + rptr) // 2
            if nums[idx] == target:
                return idx
            if target > nums[idx]:
                lptr = idx + 1
            else:
                rptr = idx - 1

        return -1


res = Solution()
print("Output -> ", res.search([-1, 0, 3, 5, 9, 12], -2))
