nums1 = [1]
nums2 = [1]
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

# Brute Force approach
# class Solution():
#     def intersect(self, nums1, nums2):
#         result = []
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] == nums2[j]:
#                     result.append(nums1[i])
#                     nums2[j] = None
#                     break
#         return result

# hash Map approach


class Solution():
    def intersect(self, nums1, nums2):
        result = []
        hashMap = {}
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        elif len(nums1) == 1 or len(nums2) == 1:
            if len(nums1) == 1:
                for i in range(len(nums2)):
                    if nums1[0] == nums2[i]:
                        result.append(nums1[0])
                        return result
            if len(nums2) == 1:
                for i in range(len(nums1)):
                    if nums2[0] == nums1[i]:
                        result.append(nums2[0])
                        return result
        else:
            for i in range(len(nums2)):
                if (nums2[i] in hashMap):
                    hashMap[nums2[i]] = hashMap.get(nums2[i]) + 1
                else:
                    hashMap[nums2[i]] = 1

            for i in range(len(nums1)):
                if(nums1[i] in hashMap):
                    result.append(nums1[i])
                    hashMap[nums1[i]] = hashMap.get(nums1[i]) - 1
                    if (hashMap[nums1[i]] == 0):
                        del hashMap[nums1[i]]

        return result


ret = Solution()
print(ret.intersect(nums1, nums2))
