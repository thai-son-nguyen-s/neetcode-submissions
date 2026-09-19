class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar = set()
        if len(sentence1) != len(sentence2):
            return False
        
        for word1, word2 in similarPairs:
            similar.add((word1, word2))
            similar.add((word2, word1))

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            if (word1, word2) not in similar:
                return False
        return True 
