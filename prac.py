class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            while len(stack) and asteroid < 0 and stack[-1] > 0:
                if stack[-1] == -asteroid: 
                    stack.pop()
                    break
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] > -asteroid:
                    break
            else:
                stack.append(asteroid)
        return stack


res = Solution()
print(res.asteroidCollision([-2,-2,1,-2]))