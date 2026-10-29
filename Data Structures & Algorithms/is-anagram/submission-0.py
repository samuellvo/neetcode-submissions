class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # track amount of characters
        seen1 = {}
        seen2 = {}
        for c in s:
            if c not in seen1:
                seen1[c] = 1
            else:
                seen1[c] = seen1[c] + 1
        for c in t:
            if c not in seen2:
                seen2[c] = 1
            else:
                seen2[c] = seen2[c] + 1
        if seen1 == seen2: 
            return True
        return False
        