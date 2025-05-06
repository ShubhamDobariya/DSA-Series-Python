# Leetcode 217 : Contains Duplicate


# Solution 1: Brute Force (Not recommended for interviews)
# Time Complexity = O(n^2)
def bruteContaiDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# Solution 2: Using Sorting
# Time Complexity = O(n long n) & Space Complexity = O(1) or O(n) depending on sorting algorithm
def sortContainDuplicate(nums):
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


# Solution 3: Using HashSet (Most Optimal)
# Time Complexity = O(n) & Space Complexity = O(n)
def optContainDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    print(bruteContaiDuplicate(nums))
    print(sortContainDuplicate(nums))
    print(optContainDuplicate(nums))
