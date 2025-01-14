class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        ln = len(s)
        if ln == 0:
            return True
        for x in t:
            if x == s[i]:
                i += 1
            if i == ln:
                return True
        return False