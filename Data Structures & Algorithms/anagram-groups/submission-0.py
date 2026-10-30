class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        # go through every word, if word is not in ans, make new entry
        # ord() returns the ordinal value; numerical representation the computer uses
        # for a character
        for word in strs:
            count = [0] * 26
            for char in word:
                # normalize offset to 0, then increment
                count[ord(char) - ord("a")] += 1
            # lists cant be keys, make tuple
            ans[tuple(count)].append(word)

        return list(ans.values())