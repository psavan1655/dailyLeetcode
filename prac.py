# function isSubsequence(s: string, t: string): boolean {
#   let sPtr = 0;

#   for (let i of t) {
#     if (s[sPtr] === i) sPtr += 1;
#   }

#   return s.length === sPtr;
# }

# console.log(isSubsequence('axc', 'ahbgdc'));


class Solution(object):
    def isSubsequence(self, s, t):
        sPtr = 0
        for i in range(len(t)):
            if sPtr == len(s):
                return True
            if s[sPtr] == t[i]:
                sPtr += 1

        return len(s) == sPtr


res = Solution()
print(res.isSubsequence("", "ahbgdc"))
