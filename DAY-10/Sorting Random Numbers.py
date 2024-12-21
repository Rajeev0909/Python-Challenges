def selection_sort(arr):
    # Perform selection sort
    for i in range(len(arr)):
        # Find the index of the smallest element in the remaining array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

random_numbers = [45, 12, 89, 33, 67, 22]
print("Random Numbers (Sorted):", selection_sort(random_numbers))
