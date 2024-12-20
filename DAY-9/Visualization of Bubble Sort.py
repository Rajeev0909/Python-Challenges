def bubble_sort_with_visualization(arr):
    n = len(arr)
    for i in range(n):
        print(f"Pass {i + 1}: {arr}")
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Numbers",numbers)
print("Sorting Visualization:")
bubble_sort_with_visualization(numbers)
