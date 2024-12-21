def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:  # Change comparison for descending order
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

numbers = [64, 25, 12, 22, 11]
print("Descending Order:", selection_sort_desc(numbers))
