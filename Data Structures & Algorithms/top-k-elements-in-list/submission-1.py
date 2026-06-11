class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        # while k > 0:
        #     ans.append(max(freq, key=freq.get))
        #     del freq[max(freq, key=freq.get)]
        #     k -= 1
        items = sorted(freq, key=freq.get, reverse=True)
        return items[:k]



        