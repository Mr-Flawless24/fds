arr = []
u = int(input("Enter the number of elements: "))
for i in range(u):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)

target = int(input("Enter the number to search for: "))

# LINEAR SEARCH
def linear_search(lst, target):
    """Perform a linear search on a list to find a target element."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

linear_result = linear_search(arr, target)
if linear_result != -1:
    print(f"Linear Search: {target} found at index {linear_result}")
else:
    print(f"Linear Search: {target} not found")

# SENTINEL SEARCH
def sentinel_search(arr, x):
    last = arr[len(arr) - 1]
    arr[len(arr) - 1] = x
    i = 0

    while arr[i] != x:
        i += 1

    arr[len(arr) - 1] = last

    if (i < len(arr) - 1) or (arr[len(arr) - 1] == x):
        return i
    else:
        return -1

sentinel_result = sentinel_search(arr, target)
if sentinel_result != -1:
    print(f"Sentinel Search: {target} found at index {sentinel_result}")
else:
    print(f"Sentinel Search: {target} not found")

