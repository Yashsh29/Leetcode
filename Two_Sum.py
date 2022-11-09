# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Link - https://leetcode.com/problems/two-sum/


def twoSum(nums, target):
    map = {}
    for i in range (len(nums)):
        comp = target - nums[i]
        if comp in map:
            return [i,map[comp]]
        map[nums[i]] = i
        

print(twoSum([2,7,11,15],9))