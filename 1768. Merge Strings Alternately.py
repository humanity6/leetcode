# Difficulty: Easy

class Solution:
    def mergeAlternately(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        new_word = ""

        diff = l1-l2
        if diff >= 1 or diff == 0:
            x = l2
        else:
            x = l1
        for i in range(x):
            new_word = new_word + word1[i] + word2[i]

        if diff == 0:
            return new_word
        elif diff >= 1:
            return new_word + word1[x:]
        else:
            return new_word + word2[x:]
        
s = Solution()
print(s.mergeAlternately("abc","pqr"))