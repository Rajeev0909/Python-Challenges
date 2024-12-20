def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr

def k_smallest_elements(arr, k):
    sorted_arr = bubble_sort(arr.copy())  # Use copy to avoid modifying the original list
    return sorted_arr[:k]

numbers = [7, 3, 8, 4, 6, 5, 2, 1]
k = 1
print("The Elements",numbers)
print(f"The  Smallest Elements:", k_smallest_elements(numbers, k))
