class Solution():
    def matrixReshape(self, mat, r, c):
        compatible = (len(mat[0]) * len(mat)) == (r*c)
        if (compatible == False):
            return mat
        else:
            newRow = 0
            newCol = 0
            reshapedMatrix = []
            reshapedMatrix.append([])
            
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if (newCol == c-1):
                        reshapedMatrix[newRow].append(mat[i][j])
                        if newRow != r-1:
                            reshapedMatrix.append([])
                        newRow += 1
                        newCol = 0
                    else:
                        reshapedMatrix[newRow].append(mat[i][j])
                        newCol += 1
            return reshapedMatrix


mat = [[1, 2], [3, 4]]
r = 1
c = 4

ret = Solution()
print(ret.matrixReshape(mat, r, c))
