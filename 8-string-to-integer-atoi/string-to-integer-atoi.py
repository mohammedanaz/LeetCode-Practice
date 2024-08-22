class Solution:
    def myAtoi(self, s: str) -> int:
         # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Step 4: Check for overflow and underflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        # Step 5: Apply the sign
        return sign * result



        # if not s:
        #     return 0
        # print('s is', s)
        # i = 0
        # start = 0
        # end = 0
        # flag_digit = 0
        # flag_sign = 0

        # while i < len(s):
        #     if s[i] == ' ':
        #         i += 1
        #         continue
        #     if s[i] in ['-', '+']:
        #         print('sign found', s[i])
        #         if flag_digit:
        #             end = i
        #             print('start and end at break', start, end)
        #             break
        #         if flag_sign:
        #             return 0
        #         flag_sign = s[i]
        #         i += 1
        #         continue
        #     if s[i].isdigit():
        #         print('digit found', s[i])
        #         print('start and end ', start, end)
        #         if not flag_digit:
        #             flag_digit = 1
        #             start = i
        #             i += 1
        #             continue
        #         i += 1
        #         continue
        #     if not s[i].isdigit():
        #         print('no digit found', s[i])
        #         if not flag_digit:
        #             return 0
        #         end = i
        #         print('start and end at break', start, end)
        #         break
        #     print('no condition met')
        #     i += 1
        # if start and end:
        #     print('result', int(s[start:end]))
        #     result = int(s[start:end]) * -1 if flag_sign == '-' else int(s[start:end])
        # if not start and end:
        #     print('result', int(s[:end]))
        #     result = int(s[:end]) * -1 if flag_sign == '-' else int(s[:end])
        # if start and not end:
        #     print('result', int(s[start:]))
        #     result = int(s[start:]) * -1 if flag_sign == '-' else int(s[start:])
        # if not start and not end:
        #     print('result', s)
        #     result = int(s) * -1 if flag_sign == '-' else int(s)
        # return -2**31 if result < -2**31 else 2**31 - 1 if result > 2**31 - 1 else result