from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        ans = []
        for key, val in reversed(sorted(counts.items(), key=lambda item: item[1])):
            ans.append(key)

        return ans[:k]
