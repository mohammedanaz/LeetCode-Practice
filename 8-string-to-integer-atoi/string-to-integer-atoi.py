class Solution:
    def myAtoi(self, s: str) -> int:
        print(f's is - ^{s}^')
        i = 0
        n = len(s)
        sign = 1
        result = 0
        int_min = -2**31
        int_max = 2**31 - 1
        if not s:
            return result
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i+=1
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            if sign * result > int_max:
                return int_max
            if sign * result < int_min:
                return int_min
            i += 1
        return sign * result
