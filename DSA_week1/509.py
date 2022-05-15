class Solution:
    def fib(self, n):
        arr = []
        arr.insert(0, 0)
        arr.insert(1, 1)
        i = 2
        while i <= n:
            arr.insert(i, arr[i - 1] + arr[i - 2])
            if i == n:
                return arr[i]
            i += 1

        print(arr)


res = Solution()
print(res.fib(3))
