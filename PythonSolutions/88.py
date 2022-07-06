class Solution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        answer = []
        i = 0
        ctr1 = 0
        ctr2 = 0
        while True:
            if(ctr1 >= m and ctr2 < n):
                answer.append(nums2[ctr2])
                ctr2 += 1
                i += 1
            elif(ctr2 >= n and ctr1 < m):
                answer.append(nums1[ctr1])
                ctr1 += 1
                i += 1
            elif(ctr1 == m and ctr2 == n):
                for j in range(0, len(nums1)):
                    nums1[j] = answer[j]
                return nums1
            else:
                if(nums1[ctr1] < nums2[ctr2]):
                    answer.append(nums1[ctr1])
                    ctr1 += 1
                    i += 1
                else:
                    answer.append(nums2[ctr2])
                    ctr2 += 1
                    i += 1


ret = Solution()
nums1 = [4, 0, 0, 0, 0, 0]

print(ret.mergeSortedArray(nums1, 1, [1, 2, 3, 5, 6], 5))
print(nums1)
# ctr1 = 0
# ctr2 = 0
# flag = True
# if (n == 0):
#     return nums1
# while flag == True:
#     if (ctr1 == m):
#         flag = False
#     if (nums1[ctr1] <= nums2[ctr2]):
#         if(nums1[ctr1] == 0):
#             for j in range(0, len(nums2)):
#                 nums1[ctr1] = nums2[j]
#                 ctr1 += 1
#             break
#         # nums1[ctr1], nums2[ctr2] = nums2[ctr2], nums1[ctr1]
#         else:
#             ctr1 += 1
#     else:
#         tmp = nums1[ctr1]
#         nums1[ctr1] = nums2[ctr2]
#         for i in range():
#             pass
#         ctr2 += 1
#         if(ctr2 == n):
#             ctr2 = 0
# return nums1
