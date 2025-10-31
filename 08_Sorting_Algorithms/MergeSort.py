# TC : O(N log₂ N)
# SC : O(N)


def Merge_Array(left, right):
    i, j = 0, 0
    n = len(left)
    m = len(right)
    result = []

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    if j < n:
        while j < m:
            result.append(right[j])
            j += 1

    return result


def Merge_Sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left_arr = nums[:mid]
    right_arr = nums[mid:]

    left = Merge_Sort(left_arr)
    right = Merge_Sort(right_arr)

    return Merge_Array(left, right)


if __name__ == "__main__":
    nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]

    print(Merge_Sort(nums))
