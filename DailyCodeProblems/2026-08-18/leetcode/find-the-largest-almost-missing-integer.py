# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Find the Largest Almost Missing Integer
# ║  Difficulty : Easy
# ║  Date       : 2026-08-18
# ║  URL        : https://leetcode.com/problems/find-the-largest-almost-missing-integer/
# ╚══════════════════════════════════════════════════════════════╝

from collections import Counter

def solve():
    """
    Problem Analysis:
    An integer 'x' is "almost missing" if it appears in exactly one subarray of size k.
    A subarray of size k starts at index i and ends at index i + k - 1.
    The total number of subarrays of size k in an array of length n is (n - k + 1).
    
    Crucial Observation:
    If an element 'x' appears multiple times within a single subarray of size k, 
    it is still counted as appearing in that subarray. However, if 'x' appears 
    in multiple different subarrays, it is not "almost missing".
    
    Algorithm:
    1. Iterate through all possible subarrays of size k.
    2. For each subarray, identify the unique elements present in it.
    3. Use a frequency map (hash table) to count how many different subarrays 
       each unique element appears in.
    4. Filter the map for elements that appeared in exactly one subarray.
    5. Return the maximum of these elements, or -1 if none exist.
    
    Time Complexity: O(n * k) 
        where n is the length of nums. We iterate (n - k + 1) times, and in each 
        iteration, we process a subarray of size k. Given constraints n <= 50, 
        this is very efficient (max 50*50 = 2500 operations).
        
    Space Complexity: O(n)
        To store the counts of elements in the hash table.
    """
    pass

class Solution:
    def largestAlmostMissingInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # count_map stores how many subarrays of size k contain the number x
        count_map = Counter()
        
        # Iterate through every subarray of size k
        for i in range(n - k + 1):
            # Extract the current subarray
            subarray = nums[i : i + k]
            
            # We only care if the element exists in the subarray, 
            # not how many times it appears within that specific subarray.
            unique_elements = set(subarray)
            
            for x in unique_elements:
                count_map[x] += 1
        
        max_almost_missing = -1
        
        # Find the largest integer that appeared in exactly one subarray
        for x, count in count_map.items():
            if count == 1:
                if x > max_almost_missing:
                    max_almost_missing = x
                    
        return max_almost_missing

# Example Usage:
# sol = Solution()
# print(sol.largestAlmostMissingInteger([3,9,2,1,7], 3)) # Output: 7
# print(sol.largestAlmostMissingInteger([3,9,7,2,1,7], 4)) # Output: 3
# print(sol.largestAlmostMissingInteger([0,0], 1)) # Output: -1
