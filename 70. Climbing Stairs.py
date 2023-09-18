# Difficulty: Easy

class Solution:

    def climbStairs(self, n: int):
        n = n + 1
        arr = [0] * n
        arr[0] = 1
        arr[1] = 1
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[-1]
    
s = Solution()
print(s.climbStairs(15))