// # class Solution:
// #     def removeDuplicates(self, nums):
// #         print(nums)
// #         i = 0
// #         arrPtr = 0
// #         val = nums[0]
// #         while i < len(nums):
// #             if nums[i] == val:
// #                 if i < len(nums) - 1:
// #                     if nums[i] != nums[i + 1]:
// #                         nums[arrPtr] = nums[i]
// #                         val = nums[i + 1]
// #                         arrPtr += 1
// #                 i += 1
// #         return nums


// # res = Solution()
// # print(res.removeDuplicates([1, 1, 2]))

// class Solution:
//     def removeDuplicates(self,s):
//         l=0
//         h=len(s)-1
//         while h > l:
//             if s[l+]


// res = Solution()
// print(res.removeDuplicates([1, 1, 2]))

const foo = (arr) => {
    // let l=0
    // let h= s.length -1
    // let f = null
    // while (h > l){
    //     if (s[l++] != s[h--]) {
    //         f = 1
    //         break
    //     }
    // }
    // if(f==1) return true
    // else  return false
    for (var i = 1; i < arr.length - 1; i++) {
        var k = arr[i]
        var j = i-1
        console.log('in', j);
        while (j>=0 &&  arr[j]>k){
            arr[j+1] = arr[j]
            j = j-1
        }
        arr[j+1] = k
    }
}

console.log(foo([1,3,4,6,8]))