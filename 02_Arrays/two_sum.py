# Two Sum (LeetCode Easy)

"""
Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers that add up to the target.
You may not use the same element twice.
"""


# Solution 1: Brute Force – O(n²) Time Complexity


def TwoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# Solution 2: Optimized using Hash Map – O(n) Time Complexity


def optTwoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(TwoSum(nums, target))
    print(optTwoSum(nums, target))
