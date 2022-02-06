class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransomNoteMap = {}
        if(len(ransomNote) > len(magazine)):
            return False
        
        for i in magazine:
            if(i in ransomNoteMap):
                ransomNoteMap[i] = ransomNoteMap[i] + 1
            else:
                ransomNoteMap[i] = 1
        for j in ransomNote:
            if(j in ransomNoteMap):
                if(ransomNoteMap[j] ==  0):
                    return False
                else:
                    ransomNoteMap[j] = ransomNoteMap[j] - 1
            else:
                return False
        return True


res = Solution()
print(res.firstUniqChar('aa', 'aab'))