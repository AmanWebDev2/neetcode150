class Solution:
    def brute(self, nums: List[int], target: int) -> List[int]:
        """
        T.C = O(n^2)
        S.C = O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return True
        return False

    def optimal(self, nums: List[int], target: int) -> List[int]:
        """
        T.C = O(n)
        S.C = O(n)
        """
        n = len(nums)
        seen = dict()

        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [i, seen.get(rem)]
            see[num] = i

        return [-1, -1]
