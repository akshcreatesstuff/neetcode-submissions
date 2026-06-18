class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        items = sorted(freq, key=freq.get, reverse = True)
        return items[:k]
        