# LeetCode : 238 - Product of Array Except Self


# Time complexity = O(2n) = O(n)
# Space complexity = O(1)


def productExceptSelf(nums):
    pre = 1
    post = 1
    res = [None] * len(nums)  # SC = O(1)

    # prefix
    for i in range(len(nums)):  # TC = O(n)
        res[i] = pre
        pre = nums[i] * pre

    # postfix
    for i in range(len(nums) - 1, -1, -1):  # TC  = O(n)
        res[i] = res[i] * post
        post = nums[i] * post

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productExceptSelf(nums))
