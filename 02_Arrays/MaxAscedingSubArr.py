# Leetcode : 1800 - MaxAscendingSubAr Maximum Ascending Subarray Sum

# Time complexity = O(n)
# Space complexity = O(1)


def MaxAscendingSubArr(arr):
    n = len(arr)
    maxSum = arr[0]
    currSum = arr[0]

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            currSum += arr[i]
        else:
            currSum = arr[i]
        maxSum = max(maxSum, currSum)

    return maxSum


if __name__ == "__main__":
    arr = [10, 20, 30, 5, 10, 50]

    print(MaxAscendingSubArr(arr))
