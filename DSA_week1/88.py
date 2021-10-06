class Solution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        ctr1 = 0
        ctr2 = 0
        flag = True
        if (n == 0):
            return nums1
        while flag == True:
            if (ctr1 == m):
                flag = False
            if (nums1[ctr1] <= nums2[ctr2]):
                if(nums1[ctr1] == 0):
                    for j in range(0, len(nums2)):
                        nums1[ctr1] = nums2[j]
                        ctr1 += 1
                    break
                # nums1[ctr1], nums2[ctr2] = nums2[ctr2], nums1[ctr1]
                else:
                    ctr1 += 1
            else:
                nums1[ctr1], nums2[ctr2] = nums2[ctr2], nums1[ctr1]
                ctr2 += 1
                if(ctr2 == n):
                    ctr2 = 0
        return nums1


ret = Solution()

print(ret.mergeSortedArray([2,0], 1, [1], 1))
