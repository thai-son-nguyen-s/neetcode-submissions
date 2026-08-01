class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        if len(s1) > len(s2):
            return False
        k = len(s1)
        l = 0
        
        for l in range(len(s2) - k + 1):
            r = l + k
            counter1 = Counter(s2[l:r])
            if count == counter1:
                return True
        
        return False
            

        

        
