class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = s.split(' ')
        length = len(arr)
        result_arr = []
        for _ in range(length):
            stripped = arr.pop().strip()
            if stripped:
                result_arr.append(stripped)
        return ' '.join(result_arr)