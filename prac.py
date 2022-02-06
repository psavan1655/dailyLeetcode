class Solution:
    def isValid(self,s):
        stack = []
        if(len(s) == 1):
            return False
        stack.append(s[0])
        for i in range(1, len(s)):
            if(len(stack) == 0):
                stack.append(s[i])
            elif(stack[-1] == '(' and s[i] == ')'):
                stack.pop()
            elif(stack[-1] == '[' and s[i] == ']'):
                stack.pop()
            elif(stack[-1] == '{' and s[i] == '}'):
                stack.pop()
            else:
                stack.append(s[i])
        
        if(len(stack) == 0):
            return True
        else:
            return False


res = Solution()
print(res.isValid("()[]{}"))