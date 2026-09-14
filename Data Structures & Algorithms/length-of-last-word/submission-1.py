class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = i = 0
        while i < len(s):
            if s[i] != ' ':
                length += 1
                i += 1
            elif s[i] == ' ':
                if i + 1 < len(s) and s[i + 1] != ' ':
                    length = 0
                i += 1
        return length