def sort_dict_by_values(d, descending=False):
    items = list(d.items())
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if (items[j][1] > items[j + 1][1]) != descending:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 88}
sorted_grades = sort_dict_by_values(grades)
print("Sorted by Values (Ascending):", sorted_grades)
sorted_grades_desc = sort_dict_by_values(grades, descending=True)
print("Sorted by Values (Descending):", sorted_grades_desc)
