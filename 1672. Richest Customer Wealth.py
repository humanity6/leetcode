# Difficulty: Easy

class Solution:
    def maximumWealth(self, accounts):
        temp = []
        for i in accounts:
            temp.append(sum(i))
        return max(temp)

s = Solution()
print(s.maximumWealth([[1,2,3],[3,2,1]]))
print(s.maximumWealth([[1,5],[7,3],[3,5]]))