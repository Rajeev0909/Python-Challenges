def remove_common_elements(set1, set2):
    return set1 - set2


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("After Removing Common Elements:", remove_common_elements(set1, set2))
