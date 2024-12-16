class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [x for x in s if x in 'aeiouAEIOU']
        print(vowels)
        lst = [x if x not in 'aeiouAEIOU' else 0 for x in s]
        print(lst)
        for i, x in enumerate(lst):
            if x == 0:
                vow = vowels.pop()
                lst[i] = vow
        print(lst)
        return ''.join(lst)        