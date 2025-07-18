# Leetcode : 268 - Missing Number

# Time complexity = O(n)
# Space complexity = O(1)


def MissingNum(arr):
    n = len(arr)

    sum = n * (n + 1) // 2
    currSum = 0

    for num in arr:
        currSum += num

    print(currSum)
    print(sum)
    return sum - currSum


if __name__ == "__main__":
    arr = [1, 0, 3]

    print(MissingNum(arr))
