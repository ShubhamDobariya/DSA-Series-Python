def binarySearch(nums, target):
    st = 0
    end = len(nums) - 1

    # Worst-case : TC = O(log n) , SC = O(log n) || Best-case : Tc = O(1)[if target is at the mid point], SC = O(1)
    while st <= end:

        mid = st + (end - st) // 2

        if target > nums[mid]:
            st = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    nums = [2, 3, 4, 10, 40]
    target = 10

    print(binarySearch(nums, target))
