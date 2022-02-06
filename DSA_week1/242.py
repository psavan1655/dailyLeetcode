class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ransomNoteMap = {}
        if(len(t) != len(s)):
            return False
        
        for i in s:
            if(i in ransomNoteMap):
                ransomNoteMap[i] = ransomNoteMap[i] + 1
            else:
                ransomNoteMap[i] = 1
        for j in t:
            if(j in ransomNoteMap):
                if(ransomNoteMap[j] ==  0):
                    return False
                else:
                    ransomNoteMap[j] = ransomNoteMap[j] - 1
            else:
                return False
        return True

res = Solution()
print(res.isAnagram('anagram', 'nagaram'))