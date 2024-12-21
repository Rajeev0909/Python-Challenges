def selection_sort_numeric_strings(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if int(arr[j]) < int(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers_as_strings = ["23", "5", "87", "12", "42"]
print("Sorted Numeric Strings:", selection_sort_numeric_strings(numbers_as_strings))
