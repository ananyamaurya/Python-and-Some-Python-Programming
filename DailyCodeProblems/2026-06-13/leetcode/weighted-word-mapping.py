# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Weighted Word Mapping
# ║  Difficulty : Easy
# ║  Date       : 2026-06-13
# ║  URL        : https://leetcode.com/problems/weighted-word-mapping/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem Analysis:
    1. We need to calculate the total weight of each word based on a given weights array.
    2. Each character in the word corresponds to an index in the weights array (a=0, b=1, ..., z=25).
    3. The word weight is the sum of weights of its characters.
    4. We take the total weight modulo 26.
    5. We map the resulting value (0-25) to a character in reverse alphabetical order:
       0 -> 'z', 1 -> 'y', ..., 25 -> 'a'.
       The formula for this mapping is: char = chr(ord('z') - value).
    6. Concatenate these characters for all words to form the final result.

    Complexity Analysis:
    - Time Complexity: O(N * L), where N is the number of words and L is the average length of a word. 
      We iterate through every character of every word exactly once.
    - Space Complexity: O(N), to store the resulting characters before joining them into the final string.
    """

    def weightedWordMapping(self, words: list[str], weights: list[int]) -> str:
        result_chars = []
        
        for word in words:
            # Calculate total weight of the word
            current_word_weight = 0
            for char in word:
                # Find index (0-25) of the current character
                char_idx = ord(char) - ord('a')
                current_word_weight += weights[char_idx]
            
            # Apply modulo 26
            mapped_val = current_word_weight % 26
            
            # Map to reverse alphabetical order:
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            # Character mapping: chr(ord('z') - mapped_val)
            mapped_char = chr(ord('z') - mapped_val)
            result_chars.append(mapped_char)
            
        # Concatenate all mapped characters into a single string
        return "".join(result_chars)

# Example usage and testing
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    words1 = ["abcd","def","xyz"]
    weights1 = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
    print(f"Example 1 Output: {sol.weightedWordMapping(words1, weights1)}") # Expected: "rij"
    
    # Example 2
    words2 = ["a","b","c"]
    weights2 = [1]*26
    print(f"Example 2 Output: {sol.weightedWordMapping(words2, weights2)}") # Expected: "yyy"
    
    # Example 3
    words3 = ["abcd"]
    weights3 = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
    print(f"Example 3 Output: {sol.weightedWordMapping(words3, weights3)}") # Expected: "g"
