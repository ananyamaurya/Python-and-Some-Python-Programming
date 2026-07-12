# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Rank Transform of an Array
# ║  Difficulty : Easy
# ║  Date       : 2026-07-12
# ║  URL        : https://leetcode.com/problems/rank-transform-of-an-array/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem: Rank Transform of an Array
    The goal is to replace each element in the array with its rank. 
    The rank is determined by the sorted order of unique elements.
    - Smallest element gets rank 1.
    - Equal elements get the same rank.
    - Ranks are consecutive integers (no gaps).
    
    Approach:
    1. Handle the empty array edge case.
    2. Create a sorted list of unique elements from the input array.
    3. Map each unique element to its rank (index in the sorted list + 1) using a hash map.
    4. Iterate through the original array and replace each value with its rank from the map.
    
    Time Complexity: O(N log N) 
        - Sorting the unique elements takes O(N log N) where N is the length of the array.
        - Mapping and transforming takes O(N).
    Space Complexity: O(N)
        - The hash map and the sorted unique list store up to N elements.
    """
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Edge case: empty array
        if not arr:
            return []
        
        # Step 1: Get unique elements and sort them
        # set() removes duplicates, sorted() returns a sorted list
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a mapping from value to rank
        # rank = index + 1 because ranks start from 1
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        
        # Step 3: Transform the original array into ranks
        # List comprehension is used for efficiency in Python
        return [rank_map[x] for x in arr]

# Example Usage and Testing:
# sol = Solution()
# print(sol.arrayRankTransform([40,10,20,30]))             # Output: [4,1,2,3]
# print(sol.arrayRankTransform([100,100,100]))           # Output: [1,1,1]
# print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12])) # Output: [5,3,4,2,8,6,7,1,3]
