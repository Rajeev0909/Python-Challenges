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

def remove_duplicates_and_sort(arr):
    unique_elements = list(set(arr))  # Remove duplicates
    return selection_sort(unique_elements)  # Sort the unique elements

numbers = [7, 3, 8, 4, 6, 3, 8, 5, 2, 1, 4]
print("Unique Sorted List:", remove_duplicates_and_sort(numbers))
