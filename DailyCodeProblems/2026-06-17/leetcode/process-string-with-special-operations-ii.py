# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Process String with Special Operations II
# ║  Difficulty : Hard
# ║  Date       : 2026-06-17
# ║  URL        : https://leetcode.com/problems/process-string-with-special-operations-ii/
# ╚══════════════════════════════════════════════════════════════╝

import sys

"""
Problem Analysis:
The final string can grow up to 10^15 characters, which is too large to construct explicitly.
We need to simulate the process in reverse to determine which character lands at index k.

Rules in forward pass:
- lowercase letter: append to string.
- '*': remove last char.
- '#': result = result + result.
- '%': result = result[::-1].

Reverse Logic:
1. We first track the length of the string after every operation in the forward pass.
2. We maintain a 'reversed' flag to track whether the current string is logically reversed.
3. We iterate backward from the end of the input string `s`.
4. Depending on the operation:
   - If it's a lowercase letter:
     Check if current k is the last character of the current string length. If so, we found it.
     Otherwise, decrement the current length.
   - If it's '*':
     The character removed by '*' is gone. The string length was effectively 1 smaller before the '*',
     but the current k remains the same relative to the start. However, we must account for the fact
     that the string grew by 1 before this '*', so we increment the "virtual" length.
   - If it's '#':
     The string was doubled. If k >= current_length // 2, then k = k - (current_length // 2).
     The length becomes current_length // 2.
   - If it's '%':
     The string was reversed. The index k becomes (current_length - 1 - k).

Complexity:
Time Complexity: O(N), where N is the length of string s. We pass through s twice.
Space Complexity: O(N) to store the lengths after each operation.
"""

class Solution:
    def kthCharacter(self, s: str, k: int) -> str:
        # Store the length of the result string after each operation
        lengths = []
        curr_len = 0
        
        for char in s:
            if 'a' <= char <= 'z':
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass # Reverse doesn't change length
            
            # Cap the length at k + 2 to avoid overflow, 
            # though problem constraints say max 10^15.
            lengths.append(curr_len)
            
        # If k is out of bounds of the final result string
        if k >= curr_len or k < 0:
            return "."
        
        # Process in reverse
        # k is 0-indexed relative to the final string
        is_reversed = False
        
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            length_before = lengths[i-1] if i > 0 else 0
            current_length = lengths[i]
            
            if char == '%':
                # The string was reversed at this step.
                # The character at index k is now the character that was at (len - 1 - k)
                k = current_length - 1 - k
            
            elif char == '#':
                # String was duplicated: result = prev + prev
                # If k falls in the second half, it maps back to the first half
                half = current_length // 2
                if k >= half:
                    k -= half
            
            elif char == '*':
                # A character was removed. This doesn't shift existing characters,
                # but we need to handle the logic that the string was longer.
                # However, since we are moving backwards, the character removed by '*'
                # is simply ignored. We don't change k.
                pass
            
            elif 'a' <= char <= 'z':
                # If the current character is the one at index k, we return it.
                # This happens if k is the last index of the string at this step.
                if k == current_length - 1:
                    return char
                # Otherwise, this character is just shifted out as we go back.
        
        return "."
