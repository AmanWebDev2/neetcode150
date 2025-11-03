class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        freq = Counter(nums)  # O(n) space and time
        arr = list()

        for item in freq.items():  # O(n)
            arr.append(item)

        # arr sort based on the freqency
        arr.sort(key=lambda x: x[1], reverse=True)  # O(nlog(n))

        return [item[0] for item in arr[:k]]  # O(k) space and time
