# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Count the Number of Special Characters II
# ║  Difficulty : Medium
# ║  Date       : 2026-05-27
# ║  URL        : https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Count the Number of Special Characters II
    
    A character is 'special' if:
    1. It appears in both lowercase and uppercase versions.
    2. All occurrences of its lowercase version appear BEFORE the first occurrence 
       of its uppercase version.
       
    Approach:
    - Track the first occurrence index of each uppercase letter.
    - Track the last occurrence index of each lowercase letter.
    - Maintain a flag or set to check if both forms actually exist.
    - A character is special if: (last_lowercase_index < first_uppercase_index).
    
    Time Complexity: O(N), where N is the length of the word. We traverse the string once.
    Space Complexity: O(1), since the storage for the 26 English letters is constant.
    """
    
    def countSpecialCharacters(self, word: str) -> int:
        # first_upper: stores the index of the first occurrence of each uppercase letter
        # last_lower: stores the index of the last occurrence of each lowercase letter
        first_upper = {}
        last_lower = {}
        
        for i, char in enumerate(word):
            if char.isupper():
                # We only care about the first time we see an uppercase letter
                if char not in first_upper:
                    first_upper[char] = i
            else:
                # We update the index every time we see a lowercase letter to get the last one
                last_lower[char] = i
        
        special_count = 0
        
        # We iterate through lowercase letters 'a' through 'z'
        for char_lower in last_lower:
            char_upper = char_lower.upper()
            
            # Condition 1: Both lowercase and uppercase must exist
            if char_upper in first_upper:
                # Condition 2: Every lowercase occurrence must appear before the first uppercase occurrence
                # This is equivalent to saying the LAST lowercase index < FIRST uppercase index
                if last_lower[char_lower] < first_upper[char_upper]:
                    special_count += 1
                    
        return special_count

# Example Trace: word = "aaAbcBC"
# i=0 'a': last_lower['a'] = 0
# i=1 'a': last_lower['a'] = 1
# i=2 'A': first_upper['A'] = 2
# i=3 'b': last_lower['b'] = 3
# i=4 'c': last_lower['c'] = 4
# i=5 'B': first_upper['B'] = 5
# i=6 'C': first_upper['C'] = 6
# 
# Checks:
# 'a': last_lower['a'](1) < first_upper['A'](2) -> Special!
# 'b': last_lower['b'](3) < first_upper['B'](5) -> Special!
# 'c': last_lower['c'](4) < first_upper['C'](6) -> Special!
# Result: 3
