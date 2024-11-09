class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Initialize total to store the integer value
        
        for i in range(len(s)):
            if i + 1 < len(s) and letters[s[i]] < letters[s[i + 1]]:
                total -= letters[s[i]]
            else:
                total += letters[s[i]]
        
        return total
