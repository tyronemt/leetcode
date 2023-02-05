# Array and Hashing
# 1: Create dictionary to store freqs of each item
# 2: Create a list with the index as the number of times a item shows up
# 3: Add elements from dictionary to list
# 4: Loop through the list backwards and add to a resulting list until result list length == the requested length

# Worst case Time Complexity is O(N)
# Space Complexity is O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        lst = []
        for i in range(len(nums) + 1):
            lst.append([])

        for i in nums:
            d[i] = 1 + d.get(i,0)
        
        for x,y in d.items():
            lst[y].append(x)
        
        res = []
        for i in range(len(lst) - 1, 0, -1):
            for j in lst[i]:
                res.append(j)
                if len(res) == k:
                    return res