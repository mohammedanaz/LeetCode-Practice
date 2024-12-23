class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_iter = min(len(word1), len(word2))
        for i in range(min_iter):
            result.append(word1[i])
            result.append(word2[i])

        result.append(word1[min_iter:] + word2[min_iter:])
        return ''.join(result)