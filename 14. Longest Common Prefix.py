# Difficulty: Easy

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        common_prefix = ""
        j = 1
        while j <= len(strs[0]):
            common_prefix = strs[0][:j]
            for string in strs:
                if string[:j] != common_prefix:
                    return strs[0][:j-1]
            j += 1
        return common_prefix

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))