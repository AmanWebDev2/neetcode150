class Solution:
    def brute(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def better(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import Counter

        return Couter(s) == Couter(t)

    def optimal(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord("a")] += 1

        for char in t:
            freq[ord(char) - ord("a")] -= 1

        for count in freq:
            if count != 0:
                return False
        return True
