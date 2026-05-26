# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Count the Number of Special Characters I
# ║  Difficulty : Easy
# ║  Date       : 2026-05-26
# ║  URL        : https://leetcode.com/problems/count-the-number-of-special-characters-i/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Count the Number of Special Characters I
    
    A character is 'special' if it appears in the given string 'word' in both 
    its lowercase and uppercase forms.
    
    Approach:
    1. Use two sets to keep track of all lowercase and uppercase letters encountered in the string.
    2. Iterate through the string once, adding each character to the respective set.
    3. The number of special characters is the size of the intersection of the two sets.
    
    Time Complexity: O(N), where N is the length of the word. We traverse the string once.
    Space Complexity: O(1), because the sets can contain at most 26 characters each regardless of input size.
    """
    
    def specialCharCount(self, word: str) -> int:
        # Set to store all lowercase letters found in the word
        lower_chars = set()
        # Set to store all uppercase letters found in the word
        upper_chars = set()
        
        for char in word:
            if char.islower():
                lower_chars.add(char)
            elif char.isupper():
                upper_chars.add(char)
        
        # We need to compare lowercase versions of both sets to find matches.
        # Convert uppercase characters to lowercase and find the intersection.
        special_count = 0
        for char in lower_chars:
            # char.upper() gives the uppercase version of the lowercase letter
            if char.upper() in upper_chars:
                special_count += 1
                
        return special_count

# Alternative one-liner approach using set intersection:
# return len(set(word.lower()) & set(word.upper()) & set(filter(str.isalpha, word))) 
# However, the explicit loop is clearer for interviews and follows the constraints precisely.
