class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        flag = False
        for i in range(len(s)):
            print(result)
            if flag:
                flag = False
                continue

            if i < len(s) - 1:
                if s[i] == 'I' and s[i+1] not in ['V', 'X']:
                    result += 1
                elif s[i] == 'I' and s[i+1] in ['V', 'X']:
                    if s[i+1] == 'V':
                        result += 4
                        flag = True
                        continue
                    else:
                        result += 9
                        flag = True
                        continue
                elif s[i] == 'V':
                    result += 5
                elif s[i] == 'X' and s[i+1] not in ['L', 'C']:
                    result += 10
                elif s[i] == 'X' and s[i+1] in ['L', 'C']:
                    if s[i+1] == 'L':
                        result += 40
                        flag = True
                        continue
                    else:
                        result += 90
                        flag = True
                        continue
                elif s[i] == 'L':
                    result += 50
                elif s[i] == 'C' and s[i+1] not in ['D', 'M']:
                    result += 100
                elif s[i] == 'C' and s[i+1] in ['D', 'M']:
                    if s[i+1] == 'D':
                        result += 400
                        flag = True
                        continue
                    else:
                        result += 900
                        flag = True
                        continue
                elif s[i] == 'D':
                    result += 500
                elif s[i] == 'M':
                    result += 1000
            else:
                if s[i] == 'I':
                    result += 1
                elif s[i] == 'V':
                    result += 5
                elif s[i] == 'X':
                    result += 10
                elif s[i] == 'L':
                    result += 50
                elif s[i] == 'C':
                    result += 100
                elif s[i] == 'D':
                    result += 500
                else:
                    result += 1000
        return result       

        