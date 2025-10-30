"""
TC = O(N(N+1)/2) = O(N²), For average & worst case
TC = O(N), for Better case

SC = O(1)

"""


def BubbleSort(nums):
    n = len(nums)

    for i in range(n - 2, -1, -1):
        is_swap = False
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True

        if is_swap == False:
            return nums


if __name__ == "__main__":
    nums = [5, 8, 1, 6, 9, 2, 4]

    print(BubbleSort(nums))
