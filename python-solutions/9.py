##########################################   Separate 2 string and then compare logic ##############################################
# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0:
#             return False
#         if x < 10:
#             return True
#         if len(str(x)) % 2 == 0:
#             firstHalf = str(x // (10 ** (len(str(x)) // 2)))
#             secondHalf = str((x % (10 ** (len(str(x)) // 2)))).zfill(
#                 len(str(firstHalf))
#             )
#             if firstHalf == "".join(reversed(secondHalf)):
#                 return True
#             return False
#         else:
#             firstHalf = str(x // (10 ** ((len(str(x)) // 2) + 1)))
#             secondHalf = str((x % (10 ** (len(str(x)) // 2)))).zfill(
#                 len(str(firstHalf))
#             )
#             print(firstHalf, secondHalf)
#             if firstHalf == "".join(reversed(secondHalf)):
#                 return True
#             return False


class Solution:
    def isPalindrome(self, x):
        startPtr = 0
        endPtr = len(str(x)) - 1
        x = str(x)
        while startPtr < endPtr:
            if x[startPtr] == x[endPtr]:
                startPtr += 1
                endPtr -= 1
            else:
                return False
        return True


res = Solution()
print(res.isPalindrome(123))
