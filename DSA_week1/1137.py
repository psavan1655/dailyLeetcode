class Solution:
    def tribonacci(self, n):
        # arr = []
        # arr.insert(0, 0)
        # arr.insert(1, 1)
        # i = 2
        # while i <= n:
        #     arr.insert(i, arr[i - 1] + arr[i - 2])
        #     if i == n:
        #         return arr[i]
        #     i += 1
        prev3 = 0
        prev2 = 1
        prev1 = 1
        if n < 2:
            return n
        if n == 2:
            return 1
        i = 3
        res = 0
        while i <= n:
            res = prev1 + prev2 + prev3
            prev1 = prev2
            prev2 = prev3
            prev3 = res
            i += 1
        return res

    def tribonacciSecondApproach(self, n):
        arr = []
        arr.insert(0, 0)
        arr.insert(1, 1)
        arr.insert(2, 1)

        if n < 3:
            return arr[n]
        i = 3
        while i <= n:
            arr.insert(i, arr[i - 1] + arr[i - 2] + arr[i - 3])
            i += 1
        return arr[n]


res = Solution()
print(res.tribonacci(4))
