class Solution(object):
    def searchInsert(self, nums, target):
        lptr = 0
        rptr = len(nums) - 1
        while rptr >= lptr:
            if target == nums[(lptr + rptr) // 2]:
                return (lptr + rptr) // 2
            if target < nums[(lptr + rptr) // 2]:
                rptr = (lptr + rptr) // 2 - 1
            if target > nums[(lptr + rptr) // 2]:
                lptr = (lptr + rptr) // 2 + 1

        return lptr


res = Solution()
print(res.searchInsert([1, 3, 5, 6], 4))
