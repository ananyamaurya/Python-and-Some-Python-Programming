# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Concatenate Non-Zero Digits and Multiply by Sum II
# ║  Difficulty : Medium
# ║  Date       : 2026-07-08
# ║  URL        : https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem Analysis:
    We need to extract a substring, remove zeros, form a number x from the remaining digits, 
    and calculate (x * sum_of_digits_of_x) modulo 10^9 + 7.
    
    Key Challenges:
    1. The number x can be very large, so we must handle it using modular arithmetic.
    2. We need to efficiently query the range [li, ri] for both the value of x and the sum.
    
    Strategy:
    - Precompute prefix sums for the digits to get the 'sum' in O(1).
    - Precompute prefix values for the non-zero digits. Since the value depends on the 
      position (power of 10), we need to track how many non-zero digits have appeared 
      up to index i.
    - Let 'nz_count[i]' be the count of non-zero digits in s[0...i-1].
    - Let 'prefix_val[i]' be the value formed by non-zero digits in s[0...i-1] modulo 10^9 + 7.
    - For a range [L, R], the number x is:
      x = (prefix_val[R+1] - prefix_val[L] * 10^(nz_count[R+1] - nz_count[L])) % MOD.
    """

    def concatenateNonZeroDigitsAndMultiplyBySum(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # prefix_sum[i] stores sum of digits in s[0...i-1]
        prefix_sum = [0] * (n + 1)
        # prefix_val[i] stores the integer formed by non-zero digits in s[0...i-1] % MOD
        prefix_val = [0] * (n + 1)
        # nz_count[i] stores the number of non-zero digits in s[0...i-1]
        nz_count = [0] * (n + 1)
        
        # Precompute powers of 10 to avoid repeated pow() calls
        # max_nz is at most n
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        for i in range(n):
            digit = int(s[i])
            prefix_sum[i+1] = prefix_sum[i] + digit
            nz_count[i+1] = nz_count[i]
            prefix_val[i+1] = prefix_val[i]
            
            if digit != 0:
                nz_count[i+1] += 1
                # Update prefix_val: shift previous value by 10 and add current digit
                prefix_val[i+1] = (prefix_val[i] * 10 + digit) % MOD
        
        results = []
        for li, ri in queries:
            # Sum of digits in the range [li, ri]
            s_val = prefix_sum[ri + 1] - prefix_sum[li]
            
            if s_val == 0:
                results.append(0)
                continue
                
            # Calculate x for the range [li, ri]
            # Number of non-zero digits in this range
            count_in_range = nz_count[ri + 1] - nz_count[li]
            
            # To extract the number from prefix_val:
            # prefix_val[ri+1] = (prefix_val[li] * 10^count_in_range + x) % MOD
            # x = (prefix_val[ri+1] - prefix_val[li] * 10^count_in_range) % MOD
            x = (prefix_val[ri + 1] - (prefix_val[li] * pow10[count_in_range]) % MOD) % MOD
            
            # The final answer is (x * sum) % MOD
            results.append((x * s_val) % MOD)
            
        return results

# Time Complexity: O(N + Q), where N is the length of the string s and Q is the number of queries.
#   - Precomputation takes O(N).
#   - Each query is answered in O(1).
# Space Complexity: O(N), to store the prefix arrays (prefix_sum, prefix_val, nz_count, and pow10).
