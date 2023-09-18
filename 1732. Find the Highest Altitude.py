# Difficulty: Easy

class Solution:
    def largestAltitude(self, gain):
        altitude = [0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            altitude[i] = altitude[i-1] + gain[i-1]
        return max(altitude)

s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))