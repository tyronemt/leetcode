# Array and Hashing
# 1: Check if the two words are the same length
# 2: Create dictionary and count all letters in the strings
# 3: Compare the two dictionaries

# Worst case Time Complexity is O(N)
# Space Complexity is O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        b = {}
        for i in range(len(s)):
            a[s[i]] = 1 + a.get(s[i],0)
            b[t[i]] = 1 + b.get(t[i],0)
        return a == b