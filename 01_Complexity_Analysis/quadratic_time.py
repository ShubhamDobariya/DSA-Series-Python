# O(n^2) - Quadratic Time Complexity
nums = [1, 2, 3]

# Nested loop → O(n^2)
for i in range(len(nums)):
    for j in range(len(nums)):
        print(f"Pair: ({nums[i]}, {nums[j]})")
