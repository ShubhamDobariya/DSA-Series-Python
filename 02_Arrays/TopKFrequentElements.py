# LeetCode: 347 - Top K Frequent Elements

from collections import Counter
import heapq

# Time Complexity = O(n) because loop iterate n time and create hashmap
# Space Complexity = O(n log k) because here we use heap instead of sorting that whay O(n log k), if we use sorting then O(n log n)


def topKFrequent(nums, k):

    # step - 1 : count frequency using build in module Counter
    count = Counter(nums)
    # Step - 2 : Create max heap Because Python’s heapq is a Min Heap, but we want a Max Heap (to get largest frequency first) that why we use '-'
    max_heap = [(-freq, num) for num, freq in count.items()]
    # Step - 3 : transforms the list into a valid heap structure
    heapq.heapify(max_heap)

    res = []

    for _ in range(k):
        freq, num = heapq.heappop(max_heap)  # first pop (-3, 1) and second pop (-2, 2)
        res.append(num)

    return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    print(topKFrequent(nums, k))
