import heapq
from collections import Counter
from typing import List


class Solution:
    def bruteForce(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(nlogn) + O(n) + O(n) + O(k) = O(nlogn)
        nlogn for sorting
        n for frequency map
        n for list
        k for answer

        Space Complexity: O(n) + O(n) + O(k) = O(n)
        n for frequency map
        n for list
        k for answer
        """
        # O(n)
        freq = Counter(nums)

        # O(n)
        l = []
        # O(n)
        for item in freq.items():
            l.append(item)

        # sort based on value - O(nlogn)
        l.sort(key=lambda x: x[1], reverse=True)

        # O(k)
        ans = []
        i = 0
        # O(k)
        while k:
            ans.append(l[i][0])
            k -= 1
            i += 1
        return ans

    def optimal(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n + nlogk)
        n for frequency map
        nlogk for heap

        Space Complexity: O(n + k)
        n for frequency map
        k for heap
        """
        # O(n)
        freq = Counter(nums)

        # O(nlogk)
        heap = []
        for num, freq in freq.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [ans[1] for ans in heap]
