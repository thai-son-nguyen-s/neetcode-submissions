class Solution:
    def confusingNumber(self, n: int) -> bool:
        reverse_map = {"1":"1", "0" : "0", "6" : "9", "8" : "8", "9" : "6" }
        
        n = str(n)
        n_reverse = []
        for i in range(len(n)):
            if n[i] not in reverse_map:
                return False
            else:
                n_reverse.append(reverse_map[n[i]])
        if n == "".join(n_reverse[::-1]):
            return False
        else:        
            return True