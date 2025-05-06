def reverse_array(arr):  # TC = O(n), SC = O(1)
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    arr = [4, 2, 7, 8, 1, 2, 5]

    reverse_array(arr)

    print(arr)
