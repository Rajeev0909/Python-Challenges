def bubble_sort_by_length(strings):
    n = len(strings)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
                swapped = True
        if not swapped:
            break
    return strings

strings = ["apple", "banana", "kiwi", "pear", "grape"]
print("Normal Strings",strings)
print("Sorted by Length:", bubble_sort_by_length(strings))
