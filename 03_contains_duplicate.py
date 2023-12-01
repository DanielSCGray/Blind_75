# 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#**************************************

#my solution will track the numbers with a hash map and return a boolean. runtime is linear O(n)


def dup_check(nums):
    tracker = {}
    for i in range(len(nums)):
        if nums[i] in tracker:
            return True
        else:
            tracker[nums[i]] = nums[i]
    return False

ex1 = [1,2,3,1]
print(dup_check(ex1))
#prints: True

ex2 = [1,2,3,4]
print(dup_check(ex2))
#prints: False

ex3 = [1,1,1,3,3,4,3,2,4,2]
print(dup_check(ex3))
#prints: True


