def findMedianOfTwoSortedArray():
    # nums1 = [2,2,2,2]
    # nums2 = [2,2,2]
    nums1 = [1]
    nums2 = [2,3,4]
    # b = [1, 15, 17, 18]

    # 1 2 3 10 15 17 18 26 21

    size = (len(nums1) + len(nums2)) % 2 == 0

    ctr1 = 0
    ctr2 = 0
    if size == True: # If block if the total length of the union array is Even
        middleElement = (len(nums1)+len(nums2))//2
        nextMiddleValue = None
        middleValue = None
        if(len(nums1) == 0):
            return (nums2[middleElement] + nums2[middleElement-1])/2
        elif len(nums2) == 0:
            return (nums1[middleElement] + nums1[middleElement-1])/2
        else:
            for i in range(0, middleElement):
                if ctr1 == len(nums1):
                    middleValue = nums2[ctr2]
                    ctr2 += 1
                elif ctr2 == len(nums2):
                    middleValue = nums1[ctr1]
                    ctr1 += 1
                elif nums1[ctr1] < nums2[ctr2]:
                    middleValue = nums1[ctr1]
                    ctr1 += 1
                else:
                    middleValue = nums2[ctr2]
                    ctr2 += 1
            if ctr1 == len(nums1):
                nextMiddleValue = nums2[ctr2]
            elif ctr2 == len(nums2):
                nextMiddleValue = nums1[ctr1]
            else:
                if nums1[ctr1] < nums2[ctr2]:
                    nextMiddleValue = nums1[ctr1]
                else:
                    nextMiddleValue = nums2[ctr2]
            print(middleValue, " test ", nextMiddleValue, "    ", (middleValue+nextMiddleValue)/2)
            return (middleValue+nextMiddleValue)/2

    else: # If block if the total length of the union array is Odd
        middleElement = (len(nums1)+len(nums2)+1)//2
        medianValue = None
        if(len(nums1) == 0):
            return nums2[middleElement-1]
        elif len(nums2) == 0:
            return nums1[middleElement-1]
        else:
            for i in range(0, middleElement):
                if ctr1 == len(nums1):
                    medianValue = nums2[ctr2]
                    ctr2 += 1
                elif ctr2 == len(nums2):
                    medianValue = nums1[ctr1]
                    ctr1 += 1
                elif nums1[ctr1] < nums2[ctr2]:
                    medianValue = nums1[ctr1]
                    ctr1 += 1
                else:
                    medianValue = nums2[ctr2]
                    ctr2 += 1
        return medianValue


print(findMedianOfTwoSortedArray())
