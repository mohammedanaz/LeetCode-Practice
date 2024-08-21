class Solution:
    def reverse(self, x: int) -> int:
        sign_flag = 0 
        if x < 0:
            sign_flag = 1
            x = x * -1
        x = int(str(x)[::-1])
        if x > 2**31:
            return 0
        return -1*x if sign_flag else x
        