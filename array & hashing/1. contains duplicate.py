class Solution:
    def brute(self,nums:List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False

    def better(self, nums: List[int]) -> bool:
        store = set()
        for num in nums:
            if num in store:
                return True
            store.add(num)
        return False