class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mobile_number_mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        combinations = ['']
        
        for digit in digits:
            temp = []
            for combination in combinations:
                for letter in mobile_number_mapping[digit]:
                    temp.append(combination + letter)
            combinations = temp
        
        return combinations

