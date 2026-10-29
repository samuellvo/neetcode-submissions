class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for x in nums:
            pair = target-x
            if pair in seen:
                return [seen[pair], i]
            if x not in seen:
                seen[x] = i
            i += 1
        return