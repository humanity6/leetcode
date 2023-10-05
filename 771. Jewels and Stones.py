class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mapp = {}
        for i in stones:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1

        count = 0
        for i in jewels:
            if i in mapp:
                count += mapp[i]

        return count



jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))

jewels = "z"
stones = "ZZ"
print(Solution().numJewelsInStones(jewels, stones))

