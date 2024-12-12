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

# FIBONACCI SEARCH
def fibonacci_search(arr, x):
    fib_M_2 = 0
    fib_M_1 = 1
    fib_M = fib_M_1 + fib_M_2

    while fib_M < len(arr):
        fib_M_2 = fib_M_1
        fib_M_1 = fib_M
        fib_M = fib_M_1 + fib_M_2

    offset = -1

    while fib_M > 1:
        i = min(offset + fib_M_2, len(arr) - 1)

        if arr[i] < x:
            fib_M = fib_M_1
            fib_M_1 = fib_M_2
            fib_M_2 = fib_M - fib_M_1
            offset = i

        elif arr[i] > x:
            fib_M = fib_M_2
            fib_M_1 = fib_M_1 - fib_M_2
            fib_M_2 = fib_M - fib_M_1

        else:
            return i

    if fib_M_1 and offset + 1 < len(arr) and arr[offset + 1] == x:
        return offset + 1

    return -1

fibonacci_result = fibonacci_search(sorted(arr), target)
if fibonacci_result != -1:
    print(f"Fibonacci Search: {target} found at index {fibonacci_result}")
else:
    print(f"Fibonacci Search: {target} not found")

# BINARY SEARCH
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

binary_result = binary_search(sorted(arr), target)
if binary_result != -1:
    print(f"Binary Search: {target} found at index {binary_result}")
else:
    print(f"Binary Search: {target} not found")
