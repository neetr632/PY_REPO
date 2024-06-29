def better_grouper(inputs, n):
    iters = [iter(inputs)] * n  # Create a list of n references to the same iterator
    return zip(*iters)  # Use zip to group elements from the same iterator

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Convert the iterator returned by zip into a list to see the grouped elements
result = list(better_grouper(nums, 2))

print(result)

