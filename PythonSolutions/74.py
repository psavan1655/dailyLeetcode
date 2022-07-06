##################################           Binary search        ############################################
# class Solution():
#     def searchMatrix(self, matrix, target):
#         for i in range(len(matrix)):
#             if(i < len(matrix) - 1):
#                 if(target == matrix[i+1][0]):
#                     return True
#                 elif (target <= matrix[i+1][0]):
#                     low = 0
#                     high = len(matrix[0])-1
#                     while low <= high:
#                         mid = (low + high) // 2
#                         num = matrix[i][mid]

#                         if num == target:
#                             return True
#                         elif num < target:
#                             low = mid + 1
#                         else:
#                             high = mid - 1
#                     return False
#             else:
#                 low = 0
#                 high = len(matrix[0])-1
#                 while low <= high:
#                     mid = (low + high) // 2
#                     num = matrix[i][mid]

#                     if num == target:
#                         return True
#                     elif num < target:
#                         low = mid + 1
#                     else:
#                         high = mid - 1
#                 return False


class Solution():
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            if(i < len(matrix) - 1):
                if(target == matrix[i+1][0]):
                    return True
                elif (target <= matrix[i+1][0]):
                    for j in range(0, len(matrix[0])):
                        if (matrix[i][j] == target):
                            return True
                    return False
            else:
                for j in range(0, len(matrix[0])):
                    if (matrix[i][j] == target):
                        return True
                return False


matrix = [[1]]
target = 1

ret = Solution()
print(ret.searchMatrix(matrix, target))
