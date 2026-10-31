class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            # concat from array to form the string, delimit with #
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        z = 0
        ans = []
        if len(s) == 0:
            return []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ans
