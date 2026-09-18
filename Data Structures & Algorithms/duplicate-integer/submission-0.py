class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if counter.get(num, 0):
                return True
            counter[num] = 1
        return False