# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Concatenate Non-Zero Digits and Multiply by Sum II
# ║  Difficulty : Medium
# ║  Date       : 2026-07-08
# ║  URL        : https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# ╚══════════════════════════════════════════════════════════════╝

import collections

"""
Problem Analysis:
- We need to find the number 'x' formed by concatenating non-zero digits of s[l..r].
- We need the sum of those digits.
- The result is (x * sum) % (10^9 + 7).
- Since s.length and queries.length are up to 10^5, an O(m + q) solution is required.

Approach:
1. Precompute the positions of all non-zero digits. This allows us to quickly identify 
   which digits in a range [l, r] contribute to 'x'.
2. Precompute a prefix sum of the digits of s to find the 'sum' in O(1).
3. To compute 'x' modulo 10^9 + 7, we use a prefix array of the non-zero digits.
   If non-zero digits are d_1, d_2, ..., d_k, then x = d_1*10^{k-1} + d_2*10^{k-2} + ... + d_k*10^0.
   Using prefix values: pref_x[i] = (pref_x[i-1] * 10 + digit) % MOD.
   The value of x for non-zero digits from index i to j is:
   x = (pref_x[j] - pref_x[i-1] * 10^(j-i+1)) % MOD.
4. We can use binary search (bisect_left/right) on the precomputed non-zero indices 
   to find the range [i, j] of non-zero digits that fall within the query range [l, r].

Time Complexity: O(m + q * log m) where m is string length and q is number of queries.
Space Complexity: O(m) to store prefix sums and positions.
"""

from bisect import bisect_left, bisect_right

class Solution:
    def solve(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # 1. Prefix sum of all digits for the 'sum' part of the query
        # pref_sum[i] is the sum of digits from s[0] to s[i-1]
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i+1] = pref_sum[i] + int(s[i])
            
        # 2. Track indices of non-zero digits and their prefix-concatenated values
        nz_indices = []
        nz_vals = [0] * (m + 1) # pref_x[i]
        
        curr_val = 0
        for i in range(m):
            digit = int(s[i])
            if digit != 0:
                nz_indices.append(i)
                curr_val = (curr_val * 10 + digit) % MOD
            nz_vals[len(nz_indices)] = curr_val
            
        # 3. Precompute powers of 10 for O(1) lookup
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        results = []
        for l, r in queries:
            # Find the range of non-zero digits that are within indices [l, r]
            # idx_l is the index in the nz_indices list for the first non-zero digit >= l
            idx_l = bisect_left(nz_indices, l)
            # idx_r is the index in the nz_indices list for the last non-zero digit <= r
            idx_r = bisect_right(nz_indices, r) - 1
            
            if idx_l > idx_r:
                # No non-zero digits found in the range
                results.append(0)
                continue
            
            # Calculate 'sum' using precomputed prefix sums
            digit_sum = pref_sum[r+1] - pref_sum[l]
            
            # Calculate 'x' using the non-zero prefix values
            # x = (nz_vals[idx_r + 1] - nz_vals[idx_l] * 10^(count_of_digits)) % MOD
            count = idx_r - idx_l + 1
            # Note: nz_vals is 1-indexed relative to nz_indices
            x = (nz_vals[idx_r + 1] - nz_vals[idx_l] * pow10[count]) % MOD
            
            results.append((x * digit_sum) % MOD)
            
        return results

# To match the LeetCode class structure expected by the platform:
# The method is actually named 'concatenateNonZeroDigitAndMultiplyBySum' in the original problem.
# Let's wrap it into the expected method name.

def concatenateNonZeroDigitAndMultiplyBySum(s: str, queries: list[list[int]]) -> list[int]:
    sol = Solution()
    return sol.solve(s, queries)
