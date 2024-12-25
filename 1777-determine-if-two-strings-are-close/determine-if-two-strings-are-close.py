from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        sort1 = sorted(freq1.values())
        sort2 = sorted(freq2.values())
        return sort1 == sort2
        