class Solution:
    def romanToInt(self, s):
        constants = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i = 0
        totalNumber = 0
        while i < len(s):
            if constants[s[i]] < (i < len(s) - 1 and constants[s[i + 1]]):
                totalNumber = totalNumber + (constants[s[i + 1]] - constants[s[i]])
                i += 2
            else:
                totalNumber = totalNumber + constants[s[i]]
                i += 1
        return totalNumber


res = Solution()
print(res.romanToInt("LVIII"))
