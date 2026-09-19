class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pointer, longest = 0, 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        while pointer < len(nums):
            i = 0
            while pointer + i + 1 < len(nums) and nums[pointer + i + 1] - nums[pointer + i] == 1:
                i += 1
            longest = max(longest, i + 1)
            pointer += max(i + 1, 1)    
            
        return longest
