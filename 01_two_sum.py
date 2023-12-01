# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#  Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exis

#*****************************************

#first solution will be the obvious one: brute force via a nested loop. O(n^2) 
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return "no two numbers in this array can be combined to equal the target"


nums_array = [3,8,4,22,0,12]

print(two_sum(nums_array, 30))
#prints [1, 3] for 8+22=30

#improved solution will use a hashmap to track number-index info as key-value pairs for a runtime of O(n)

def hashed_two_sum(nums, target):
    nums_hash = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in nums_hash:
            return [nums_hash[difference], i]
        else:
            nums_hash[nums[i]] = i
    return "no two numbers in this array can be combined to equal the target"

print(hashed_two_sum(nums_array, 25))
#prints [0, 3] for 3+22=25