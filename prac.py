class Solution:
    def peakIndexInMountainArray(self, arr):
        print(' arr => ', arr)
        prev = arr[0]
        for i in range(len(arr)):
            if(prev > arr[i]):
                return i-1
            prev = arr[i]
        

res = Solution()
print(res.peakIndexInMountainArray([0,1,0]))