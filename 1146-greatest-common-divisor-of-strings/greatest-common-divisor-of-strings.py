class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        a = len(str1)
        b = len(str2)
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        slc = gcd(a, b)
        return str1[:slc]
        