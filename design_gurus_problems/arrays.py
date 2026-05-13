import math

#? The running sum at position i in the new array is calculated as the sum of all the numbers 
#? in the original array from the 0th index up to the i-th index (inclusive).
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
def running_sum(nums):
    new_list = []
    sum = 0
    for num in nums:
        sum = sum + num
        new_list.append(sum)
    
    return new_list

#? Given an integer array nums, return true if any value appears at least twice in the array, 
#? and return false if every element is distinct.
# Input: [1,2,3,4]
# Output: false
def contains_duplicate(nums):  # Brute force approach
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)): # Start checking AFTER the current index
            if num == nums[j]:
                return True

    return False

def contains_duplicate_v2(nums):
    seen_nums_dict = {}
    for num in nums:
        #check that a num exists in dictionary
        if num in seen_nums_dict:
            return True
        else:
            seen_nums_dict[num] = 1
    return False

#? Given an input array of integers nums, find an integer array, let's call it differenceArray, 
#? of the same length as an input integer array.
# differenceArray[i] = | leftSumi - rightSumi |
# Input: [2, 5, 1, 6, 1]
# Output: [13, 6, 0, 7, 14]

# Explanation:
# - For i=0: |(0) - (5+1+6+1)| = |0 - 13| = 13
# - For i=1: |(2) - (1+6+1)| = |2 - 8| = 6
def find_difference_array(nums):
    difference_array = []

    for i, num in enumerate(nums):

        left_side_sum = 0
        right_side_sum = 0

        # Left side
        for j in range(i - 1, -1, -1):
            left_side_sum += nums[j]

        # Right side
        for j in range(i + 1, len(nums)):
            right_side_sum += nums[j]

        result = abs(left_side_sum - right_side_sum)

        difference_array.append(result)

    return difference_array

#? You are given an mxn matrix accounts where accounts[i][j] is the amount of money the ith customer
# has in the jth bank
# Return the wealth that the richest customer has 

def maximum_wealth(accounts):
    max_wealth = 0
    for customer_accounts in accounts:
        wealth = 0
        for money in customer_accounts:
            wealth += money

        if wealth > max_wealth:
            max_wealth = wealth
            
    return max_wealth