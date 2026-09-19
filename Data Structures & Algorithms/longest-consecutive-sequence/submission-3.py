class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                length = 0
                current = 0
                while num + current in nums:
                    length += 1
                    current += 1
                longest = max(longest, length)
        return longest

