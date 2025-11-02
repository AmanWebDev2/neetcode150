class Solution:
    def brute(self, strs: List[str]) -> List[List[str]]:
        """
        T.C = O(n * klogk)
        S.C = O(n * k)
        """
        from collections import defaultdict

        seen = defaultdict(list)

        for word in strs:
            seen[tuple(sorted(word))].append(word)

        print(seen.values())
        return list(seen.values())

    def optimal(self, strs: List[str]) -> List[List[str]]:
        """
        T.C = O(n * k)
        S.C = O(n * k)
        """
        from collections import defaultdict

        seen = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord("a")] += 1

            seen[tuple(freq)].append(word)

        return list(seen.values())
