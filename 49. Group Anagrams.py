# Difficulty: Medium

class Solution:
    def groupAnagrams(self, strs):
        map = {}
        for word in strs:
            sword = "".join(sorted(word))
            if sword in map:
                map[sword].append(word)
            else:
                map[sword] = [word]
        return list(map.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))