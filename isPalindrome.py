# Worst case Time Complexity is O(N)
# Space Complexity is O(1)

class Solution:
    def is_alphanumeric(self, c):               # function to check if the character is 
                                                # alphanumeric
        return (ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1                     # using two pointers

        while l < r:                                          # skip all the characters 
                                                              # that are not alphanumeric
            while l < r and not self.is_alphanumeric(s[l]):
                l += 1
            while l < r and not self.is_alphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():                  # compare characters from both pointers
                return False
            l += 1
            r -= 1
        return True
    
