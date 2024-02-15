
# 53. Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.



# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.




def max_sub_sum(array):
    i = 0 
    greatest_sum = 0
    current_sum =0 
    while i < len(array)-1:
        if array[i] < 0:
            current_sum = 0 
            i+=1 
            continue
        current_sum = array[i]
        if current_sum > greatest_sum:
            greatest_sum = current_sum
        j = i + 1 
        while j < len(array):
            current_sum += array[j]
            if current_sum > greatest_sum:
                greatest_sum = current_sum
            elif current_sum < 0:
                i = j 
                break
            #if j has fully iterated the list w/out hitting the elif above, then there is no distinctive sub array and the evalution process is complete. i is advanced to prevent redundant loops and preserve runtime
            if j == len(array) -1:
                i = j 
                break
            j += 1
        i += 1
    #i stopping at one idx before len(array) -1 creates an edge case where, if the last value alone is the greatest subarray, it could be overlooked - the if below solves for that
    if array[-1] > greatest_sum:
        greatest_sum = array[-1]
    return greatest_sum

print(max_sub_sum([-2,1,-3,4,-1,2,1,-5,4]))
#6
print(max_sub_sum([1]))
#1
print(max_sub_sum([5,4,-1,7,8]))
#23
