class Solution(object):
    def isIsomorphic(self, s, t):
        hashes = {}
        reservedChars = []
        for i in range(len(s)):
            if s[i] in hashes:
                if hashes[s[i]] != t[i]:
                    return False
            else:
                if t[i] in reservedChars:
                    return False
                hashes[s[i]] = t[i]
                reservedChars.append(t[i])
        return True


res = Solution()
print(res.isIsomorphic("badc", "baba"))
