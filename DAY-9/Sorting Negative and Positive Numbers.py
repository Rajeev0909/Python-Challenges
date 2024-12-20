def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements
    return arr

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements in reverse order
    return arr

def sort_negative_positive(arr):
    negatives = [num for num in arr if num < 0]
    positives = [num for num in arr if num >= 0]

    negatives = bubble_sort_desc(negatives)  # Sort negatives in descending order
    positives = bubble_sort(positives)  # Sort positives in ascending order

    return negatives + positives

numbers = [3, -2, -7, 5, 1, -4, 6, -3]
print("Numbers",numbers)
print("Sorted Negatives and Positives Numbers:", sort_negative_positive(numbers))

