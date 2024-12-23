class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        iter_value = min(len(word1), len(word2))
        lst1 = [x for x in word1]
        lst1.reverse()
        lst2 = [x for x in word2]
        lst2.reverse()
        for i in range(iter_value):
            pop1 = lst1.pop()
            pop2 = lst2.pop()
            result.extend([pop1, pop2])
        if lst1:
            lst1.reverse()
            result.extend(lst1)
        if lst2:
            lst2.reverse()
            result.extend(lst2)
        return ''.join(result)