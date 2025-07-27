from collections import defaultdict
from typing import List


class Solution:
    def approach2(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(N * K)
        Space Complexity: O(N * K)
        where N is the number of words in the input list, and K is the maximum length of a word.
        """
        mpp = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            mpp[tuple(count)].append(word)
        return list(mpp.values())

    def approach1(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(N * K * log(K))
        Space Complexity: O(N * K)
        We are storing n sorted words in the map of average length k.
        """
        mpp = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            mpp[sorted_word].append(word)
        return list(mpp.values())

    def approach3(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(N * K * log(K))
        Space Complexity: O(N * K)
        We are storing n sorted words in the map of average length k.
        """
        mpp = defaultdict(list)
        for word in strs:
            mpp[tuple(sorted(word))].append(word)
        return list(mpp.values())
