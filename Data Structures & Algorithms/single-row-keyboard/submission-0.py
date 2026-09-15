class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashtable = {}
        position = ans = 0
        
        for i in range(len(keyboard)):
            val = keyboard[i]
            hashtable[val] = i
        for j in range(len(word)):
            step = abs(hashtable[word[j]] - position)
            position = hashtable[word[j]]
            ans = ans + step
        return ans
