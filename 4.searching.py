arr = [1,25,3,5,6]

# LINEAR SEARCH
def linear_search(lst, target):
    """Perform a linear search on a list to find a target element."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
print(linear_search(arr, 5))

# SENTINAL SEARCH
def sentinelsearch(arr,x):
    last = arr[len(arr)-1]
    
    arr[len(arr)-1] = x
    i = 0
    
    while(arr[i] != x):
         i += 1
          
    arr[len(arr)-1] = last
    
    if((i<len(arr)-1) or (arr[len(arr)-1] == x)):
       print(x,"is present at index ",i)
    else:
        print("element not found")
           
arr = [1,25,3,5,6]
print(sentinelsearch(arr,25))


# FIBONACCI SEARCH
def fibonacci_search(arr, x):
    fib_M = 0
    fib_M_1 = 1
    fib_M_2 = 0

    while (fib_M < len(arr)):
        fib_M_2 = fib_M_1
        fib_M_1 = fib_M
        fib_M = fib_M_1 + fib_M_2

    offset = -1

    while (fib_M > 1):
        i = min(offset + fib_M_2, len(arr) - 1)

        if (arr[i] < x):
            fib_M = fib_M_1
            fib_M_1 = fib_M_2
            fib_M_2 = fib_M - fib_M_1
            offset = i

        elif (arr[i] > x):
            fib_M = fib_M_2
            fib_M_1 = fib_M_1 - fib_M_2
            fib_M_2 = fib_M - fib_M_1

        else:
            return i

    if (fib_M_1 and arr[offset + 1] == x):
        return offset + 1

    return -1

# print(fibonacci_search(arr, 5))


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

arr.sort()
print("Binary Search Index: ", binary_search(arr, 5))


