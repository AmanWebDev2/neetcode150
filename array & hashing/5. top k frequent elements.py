class Solution:
    def brute(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        freq = Counter(nums)  # O(n) space and time
        arr = list()

        for item in freq.items():  # O(n)
            arr.append(item)

        # arr sort based on the freqency
        arr.sort(key=lambda x: x[1], reverse=True)  # O(nlog(n))

        return [item[0] for item in arr[:k]]  # O(k) space and time

    def better(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freq = Counter(nums)  # O(n)

        heap = []
        heapq.heapify(heap)

        for num, occ in freq.items():  # O(n)
            heapq.heappush(heap, (occ, num))  # O(logk)
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]  # O(k)
