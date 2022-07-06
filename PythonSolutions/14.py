class Solution:
    def longestCommonPrefix(self, strs):
        prefixStr = ""
        charPtr = 0
        while True:
            tmpStr = ""
            i = 0
            for i in range(len(strs)):
                if charPtr == (len(strs[i])):
                    return prefixStr
                if i == 0:
                    tmpStr = strs[i][charPtr]
                if strs[i][charPtr] != tmpStr:
                    return prefixStr
                if i == (len(strs) - 1):
                    prefixStr = prefixStr + (strs[i][charPtr])
                    charPtr += 1


res = Solution()
print(res.longestCommonPrefix([""]))
