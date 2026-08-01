class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = Counter(s)
        hash2 = Counter(t)
        if len(s) == len(t) and hash1 == hash2:
            return True
        else:
            return False