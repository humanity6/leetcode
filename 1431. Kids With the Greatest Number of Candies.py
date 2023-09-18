# Difficulty: Easy

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        most = max(candies)
        temp = []
        for i in candies:
            if i + extraCandies >= most:
                temp.append(True)
            else:
                temp.append(False)

        return temp

s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
print(s.kidsWithCandies([4,2,1,1,2], 1))