# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Process String with Special Operations I
# ║  Difficulty : Medium
# ║  Date       : 2026-06-16
# ║  URL        : https://leetcode.com/problems/process-string-with-special-operations-i/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Process String with Special Operations I
    
    The goal is to simulate the construction of a string based on a set of 
    special characters:
    - lowercase letter: append to result.
    - '*': pop the last character (backspace).
    - '#': double the current string (result = result + result).
    - '%': reverse the current string.
    
    Since the constraint on the input string length is very small (s.length <= 20),
    a direct simulation using a list of characters (which allows efficient 
    appending and popping) is optimal.
    
    Time Complexity: O(N * L), where N is the length of the input string s and 
                     L is the maximum length the result string can reach. 
                     Given N=20, the length can grow exponentially due to '#', 
                     but is manageable for these constraints.
    Space Complexity: O(L), where L is the length of the final result string.
    """

    def processString(self, s: str) -> str:
        # Use a list to store characters of the result for efficient modification
        result = []
        
        for char in s:
            if 'a' <= char <= 'z':
                # Rule 1: Lowercase English letter - append to result
                result.append(char)
            elif char == '*':
                # Rule 2: '*' - remove last character if result is not empty
                if result:
                    result.pop()
            elif char == '#':
                # Rule 3: '#' - duplicate the current result
                # We extend the list by its current contents
                result.extend(result[:])
            elif char == '%':
                # Rule 4: '%' - reverse the current result
                # Reverse the list in-place
                result.reverse()
        
        # Join the list of characters into a final string
        return "".join(result)

# Example usage:
# sol = Solution()
# print(sol.processString("a#b%*")) # Expected: "ba"
# print(sol.processString("z*#"))   # Expected: ""
