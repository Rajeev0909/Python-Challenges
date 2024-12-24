def linear_search(arr, target):
    """
    Perform a Linear Search on a list.
    
    Parameters:
    - arr: List of elements to search in.
    - target: Value to search for.
    
    Returns:
    - Index of the target if found, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [10, 20, 30, 40, 50]
target = 30
print("Target Found at Index:", linear_search(numbers, target))
