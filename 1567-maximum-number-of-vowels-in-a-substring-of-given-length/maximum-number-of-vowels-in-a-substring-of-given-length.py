class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_count = 0
        temp_count = 0
        for i in range(k):
            if s[i] in vowels:
                temp_count += 1
        max_count = temp_count
        if max_count == k:
            return k
        for i in range(k, len(s)):
            if s[i] in vowels:
                temp_count += 1
            if s[i - k] in vowels:
                temp_count -= 1
            max_count = max(max_count, temp_count)
            if max_count == k:
                return k
        return max_count