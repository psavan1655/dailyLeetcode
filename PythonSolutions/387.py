class Solution:
    def firstUniqChar(self, s):
        print(s)
        hashMap = {}
        for i in s:
            if(i in hashMap):
                hashMap[i] = 1
            else:
                hashMap[i] = 0
        for i in range(len(s)):
            if hashMap[s[i]] == 0:
                return i
        return -1

res = Solution()
print(res.firstUniqChar('test'))