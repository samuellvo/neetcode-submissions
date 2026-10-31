class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        # two arrays, one for everything before i and one for everything after i
        left = [1] * len(nums)
        right = [1] * len(nums)
        # make left array
        while i < len(nums):
            left[i] = left[i-1] * nums[i-1]
            i += 1

        # make right array
        rev_copy = nums[::-1]
        i = 1
        while i < len(nums):
            right[i] = right[i-1] * rev_copy[i-1]
            i += 1
        right_rev = right[::-1]
        ans = [1] * len(nums)
        i = 0
        while i < len(nums):
            ans[i] = left[i] * right_rev[i]
            i += 1
        return ans

