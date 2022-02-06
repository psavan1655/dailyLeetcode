class Solution():
    def generate(self, numRows):
        pascals = []
        for i in range(numRows):
            pascals.append([])
            if i == 0:
                pascals[0].append(1)
            else:
                for j in range(0, i+1):
                    if j == 0 or j == i:
                        pascals[i].append(pascals[i-1][0])
                    else:
                        pascals[i].append(pascals[i-1][j-1] + pascals[i-1][j])
        return pascals

ret = Solution()
numRows = 5
print(ret.generate(numRows))