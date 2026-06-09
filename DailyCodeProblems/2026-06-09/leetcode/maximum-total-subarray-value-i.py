# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Maximum Total Subarray Value I
# ║  Difficulty : Medium
# ║  Date       : 2026-06-09
# ║  URL        : https://leetcode.com/problems/maximum-total-subarray-value-i/
# ╚══════════════════════════════════════════════════════════════╝

import heapq

"""
Problem Analysis:
We need to choose exactly k subarrays. Each subarray's value is max(subarray) - min(subarray).
Since subarrays can overlap and be chosen multiple times, the goal is to maximize the sum 
of these differences.

Key Insight:
The maximum possible value for any subarray is (global_max - global_min) of the entire array.
If we can find a subarray that contains both the global maximum and global minimum, 
its value is (max(nums) - min(nums)). If we pick this same subarray k times, 
the total value is k * (max(nums) - min(nums)).

Is it always possible to achieve k * (max(nums) - min(nums))?
- If n = 1, the difference is always 0, so the result is 0.
- If n > 1, we can always find at least one subarray (even the whole array) 
  that contains both the maximum and minimum elements of the array.
  Let max_val = max(nums) and min_val = min(nums).
  The value of the subarray containing both is (max_val - min_val).
  Since we can choose the same subarray k times, the total sum is k * (max_val - min_val).

Wait, is there any constraint that prevents us from picking the same subarray?
The problem states: "Subarrays may overlap, and the exact same subarray (same l and r) 
can be chosen more than once." This means we can simply pick the subarray that 
contains both the global maximum and minimum k times.

Complexity:
- Time Complexity: O(n), where n is the length of the array, to find the max and min.
- Space Complexity: O(1), as we only store a few integer variables.
"""

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        """
        Returns the maximum total value of k chosen subarrays.
        
        The optimal strategy is to find the maximum and minimum elements in the 
        array and form a subarray that contains both. The value of such a 
        subarray is (max(nums) - min(nums)). By choosing this specific 
        subarray k times, we maximize the total value.
        """
        if not nums:
            return 0
        
        # Find the global maximum and minimum in the array
        max_val = max(nums)
        min_val = min(nums)
        
        # The maximum value for a single subarray is (max_val - min_val).
        # We can pick this subarray k times.
        return k * (max_val - min_val)

# Example test cases to verify logic:
# Example 1: nums = [1, 3, 2], k = 2
# max = 3, min = 1 -> 2 * (3 - 1) = 4. Correct.
# Example 2: nums = [4, 2, 5, 1], k = 3
# max = 5, min = 1 -> 3 * (5 - 1) = 12. Correct.
