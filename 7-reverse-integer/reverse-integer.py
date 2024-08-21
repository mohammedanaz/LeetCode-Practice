class Solution:
    def reverse(self, x: int) -> int:
        sign_flag = 0 if x >= 0 else 1
        x_string = str(abs(x))
        print(sign_flag)
        print(x_string)
        x = x_string[::-1] if sign_flag == 0 else '-' + x_string[::-1]
        x = int(x)
        return x if -2**31 <= x <= 2**31 - 1 else 0
        