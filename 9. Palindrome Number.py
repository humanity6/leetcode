# Difficulty: Easy

class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))