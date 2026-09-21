class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        feed = i = j = 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                feed += 1
                i += 1
            j += 1
        return feed