class Solution:
    def isValid(self, s: str) -> bool:
        collection = []
        close_bracket = {']':'[', '}':'{', ')':'('}

        for char in s:
            if char not in close_bracket:
                collection.append(char)
            else:
                latest_open_bracket = collection.pop() if collection else None
                if latest_open_bracket != close_bracket[char]:
                    return False
        return not collection
        
                        
