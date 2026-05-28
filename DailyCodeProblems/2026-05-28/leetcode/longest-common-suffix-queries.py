# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Longest Common Suffix Queries
# ║  Difficulty : Hard
# ║  Date       : 2026-05-28
# ║  URL        : https://leetcode.com/problems/longest-common-suffix-queries/
# ╚══════════════════════════════════════════════════════════════╝

import collections

"""
Problem Analysis:
The goal is to find a string in wordsContainer that shares the longest common suffix with a given query string.
Ties are broken by:
1. Shortest length of the candidate string in wordsContainer.
2. Smallest index of the candidate string in wordsContainer.

Since we are dealing with suffixes, we can reverse all strings in wordsContainer and the query strings, 
turning the "longest common suffix" problem into a "longest common prefix" problem.
A Trie (Prefix Tree) is the ideal data structure for prefix matching.

Approach:
1. Reverse every string in wordsContainer.
2. Insert these reversed strings into a Trie.
3. Each node in the Trie will store the 'best' index. The 'best' index is defined by 
   the criteria: (length of word, original index). We want to minimize this pair.
4. For each query string:
    a. Reverse it.
    b. Traverse the Trie as far as the characters of the reversed query match.
    c. The last node reached before a mismatch (or the end of the query/Trie path) holds 
       the index of the best string sharing the longest prefix.

Time Complexity:
- Building the Trie: O(Sum of lengths of strings in wordsContainer).
- Querying the Trie: O(Sum of lengths of strings in wordsQuery).
- Total: O(S_container + S_query), where S is the total sum of lengths.

Space Complexity:
- Trie Storage: O(S_container * 26) in worst case, though realistically much less.
"""

class TrieNode:
    def __init__(self):
        # children stores mapped characters to TrieNodes
        self.children = {}
        # best_idx stores the index of the string that is the "best" 
        # among all strings passing through this node.
        self.best_idx = -1

class Solution:
    def longestCommonSuffixQueries(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        
        # Step 1: Populate the Trie with reversed words from wordsContainer
        for idx, word in enumerate(wordsContainer):
            # We process the word in reverse to treat suffix as prefix
            reversed_word = word[::-1]
            curr = root
            
            # The root represents an empty suffix. All words share it.
            # Update the root's best_idx based on the criteria: (length, index)
            if curr.best_idx == -1 or \
               len(word) < len(wordsContainer[curr.best_idx]) or \
               (len(word) == len(wordsContainer[curr.best_idx]) and idx < curr.best_idx):
                curr.best_idx = idx
            
            for char in reversed_word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update best_idx at this node
                # If this word is shorter than the current best word at this node, 
                # or equal length but smaller index, it becomes the new best.
                if curr.best_idx == -1 or \
                   len(word) < len(wordsContainer[curr.best_idx]) or \
                   (len(word) == len(wordsContainer[curr.best_idx]) and idx < curr.best_idx):
                    curr.best_idx = idx
        
        results = []
        
        # Step 2: Process each query
        for query in wordsQuery:
            reversed_query = query[::-1]
            curr = root
            best_found = root.best_idx
            
            for char in reversed_query:
                if char in curr.children:
                    curr = curr.children[char]
                    best_found = curr.best_idx
                else:
                    # No more matching characters, the last node reached is the 
                    # longest common suffix match.
                    break
            
            results.append(best_found)
            
        return results
