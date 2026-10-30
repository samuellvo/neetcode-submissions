class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        if len(nums) == 1:
            return [nums[0]]
        # dictionary, key-val, key is the unique num
        for x in nums:
            if x not in ans:
                ans[x] = 1
            else:
                ans[x] += 1
        return list(sorted(ans, key= lambda x: ans[x], reverse = True))[:k]