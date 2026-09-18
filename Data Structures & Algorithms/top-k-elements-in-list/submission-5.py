class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        n = len(nums)
        bucket = [[] for i in range(n + 1)]
        for key, val in counts.items():
            bucket[val].append(key)
        res = []
        for i in range(n, -1, -1):
            res.extend(bucket[i])
        return res[:k]

        
