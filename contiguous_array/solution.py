class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}
        max_length = 0
        accum = 0

        for i, num in enumerate(nums):
            accum += num if num == 1 else -1
            if accum in mp:
                max_length = max(max_length, i - mp[accum])
            else:
                mp[accum] = i

        return max_length
