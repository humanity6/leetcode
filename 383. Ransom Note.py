# Difficulty: Easy

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        return len(Counter(ransomNote) - Counter(magazine)) == 0
    
s = Solution()
print(s.canConstruct("aa","aab"))