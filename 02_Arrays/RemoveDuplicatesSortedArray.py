# leetCode : 26 - Remove Duplicates from Sorted Array

# Time complexity = O(n)
# Space complexity = O(1) beacause in-placed, no extra array or list used


def remove_duplicates(nums):

    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):

        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3]

    print(remove_duplicates(nums))
