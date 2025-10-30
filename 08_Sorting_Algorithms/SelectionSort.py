# TC : O(N(N+1)/2) = O(n²), where N is length of nums
# SC : O (1)


def SelectionSort(nums):
    n = len(nums)

    for i in range(0, n):
        min_idx = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == "__main__":
    nums = [5, 7, 8, 4, 1, 6, 9, 2]

    print(SelectionSort(nums))
