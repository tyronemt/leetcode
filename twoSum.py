# Array and Hashing
# 1: Create dictionary to store target - current number
# 2: Go through each index
# 3: Check if the current number is in the dictionary
# 4: If the current number is not in the dictionary then subtract it from the target and attached its product to the dictionary's keys

# Worst case Time Complexity is O(N)
# Space Complexity is O(N)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                temp = target - nums[i]
                dic[temp] = i