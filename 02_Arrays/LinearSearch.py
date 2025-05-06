def linearSearch(nums, target):  # TC = O(n)

    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


if __name__ == "__main__":
    nums = [4, 2, 7, 8, 1, 2, 5]
    target = 8

    print(linearSearch(nums, target))
