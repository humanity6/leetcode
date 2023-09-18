# Difficulty: Easy

class Solution:
    def plusOne(self, digits):
        i = -1
        while digits[i] == 9:

            digits[i] = 0
            i -= 1
            if i < -len(digits):
                break
            
        if i < -len(digits):
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits
    
s = Solution()
print(s.plusOne([9,9,9]))