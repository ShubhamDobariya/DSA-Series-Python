"""
TC = O(N/2) = 1/2 * O(N)
   = O(N)

SC = O(N/2) = 1/2 * O(N)
   = O(N) due to stack space
"""


def ReverseFunc(nums, left, right):
    # Base Case
    if left >= right:
        return

    nums[left], nums[right] = nums[right], nums[left]
    ReverseFunc(nums, left + 1, right - 1)


def ReverseArray(nums, left, right):
    # call ReverseFun
    ReverseFunc(nums, left, right)
    return nums


if __name__ == "__main__":
    nums = [5, 7, 3, 2, 6, 1, 5, 9]
    left = 2
    right = 5
    # we can reverse some portion of an array using left and right
    print(ReverseArray(nums, left, right))
