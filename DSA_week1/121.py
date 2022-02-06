import sys

################################################### Time complexity more, But less space complexity ###########################################
# class Solution():
#     def maxProfit(self, prices):
#         profit = 0
#         processedArr = []
#         if len(prices) == 0:
#             return 0
#         else:
#             min = []
#             minValue = 0
#             maxArr = []
#             maxValue = None
#             for i in range(len(prices)):
#                 if i == 0:
#                     minValue = prices[0]
#                     min.append(minValue)
#                     maxValue = prices[len(prices)-1]
#                     maxArr.append(maxValue)
#                 else:
#                     if (prices[i] < minValue):
#                         minValue = prices[i]
#                         min.append(minValue)
#                     else:
#                         min.append(minValue)

#                     if (prices[len(prices) - i - 1] > maxValue):
#                         maxValue = prices[len(prices) - i - 1]
#                         maxArr.append(maxValue)
#                     else:
#                         maxArr.append(maxValue)
#             maxArr.reverse()
#             # for i in range(len(prices)):
#             #     processedArr.append(maxArr[i] - min[i])
#             profit = max(maxArr - min)
#         return profit


# class Solution():
#     def maxProfit(self, prices):
#         buyPrice = prices[0]
#         sellPrice = prices[0]
#         maxProfit = sellPrice-buyPrice

#         for i in range(0, len(prices)):
#             buyPrice = min(prices[i], buyPrice)
#             sellPrice = max(prices[i], sellPrice)
#             maxProfit = max(prices[i]-buyPrice, maxProfit)

#         return maxProfit


class Solution():
    def maxProfit(self, prices):
        maxCurr = 0
        minCurr = sys.maxsize
        for i in range(len(prices)):
            if (prices[i] < minCurr):
                minCurr = prices[i]
            elif (prices[i] > minCurr):
                maxCurr = max(prices[i] - minCurr, maxCurr)
        return maxCurr


# prices = [7, 6, 4, 3, 1]
prices = [7, 1, 5, 3, 6, 4]

ret = Solution()
print(ret.maxProfit(prices))
