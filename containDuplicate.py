# Array and Hashing
# 1: Create hashset so that search time is O(1)
# 2: Run through nums list to see if the number already exist in our hashset

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False